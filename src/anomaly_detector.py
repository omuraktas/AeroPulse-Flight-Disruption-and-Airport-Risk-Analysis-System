import numpy as np


class AnomalyDetector:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def detect_daily_anomalies(self):

        daily = self.df.groupby("fl_date").agg(
            average_delay=("arr_delay", "mean"),
            total_flights=("fl_date", "size")
        )

        values = daily["average_delay"].dropna().to_numpy()

        mean = np.mean(values)
        std = np.std(values)

        daily["z_score"] = (
            daily["average_delay"] - mean
        ) / std

        # Sadece normalden ciddi şekilde kötü günleri al
        anomalies = daily[
            daily["z_score"] >= 2
        ].copy()

        # Normal ortalamaya göre kaç dakika daha kötü?
        anomalies["above_normal_minutes"] = (
            anomalies["average_delay"] - mean
        )

        # Anomaly seviyesi
        conditions = [
            anomalies["z_score"] >= 4,
            anomalies["z_score"] >= 3
        ]

        levels = [
            "CRITICAL",
            "VERY HIGH"
        ]

        anomalies["anomaly_level"] = np.select(
            conditions,
            levels,
            default="HIGH"
        )

        return anomalies.sort_values(
            "z_score",
            ascending=False
        )

    def investigate_day(self, date):

        day_data = self.df[
            self.df["fl_date"] == date
        ].copy()

        day_data["route"] = (
            day_data["origin"]
            + " -> "
            + day_data["dest"]
        )

        # Havayolları
        airlines = day_data.groupby(
            "op_unique_carrier"
        ).agg(
            total_flights=("op_unique_carrier", "size"),
            average_delay=("arr_delay", "mean")
        ).sort_values(
            "average_delay",
            ascending=False
        )

        # Havalimanları
        airports = day_data.groupby(
            "origin"
        ).agg(
            total_flights=("origin", "size"),
            average_delay=("dep_delay", "mean")
        ).sort_values(
            "average_delay",
            ascending=False
        )

        # Saatler
        hours = day_data.groupby(
            "departure_hour"
        ).agg(
            total_flights=("departure_hour", "size"),
            average_delay=("arr_delay", "mean")
        ).sort_values(
            "average_delay",
            ascending=False
        )

        # Rotalar
        routes = day_data.groupby(
            "route"
        ).agg(
            total_flights=("route", "size"),
            average_delay=("arr_delay", "mean")
        )

        routes = routes[
            routes["total_flights"] >= 5
        ].sort_values(
            "average_delay",
            ascending=False
        )

        return airlines, airports, hours, routes