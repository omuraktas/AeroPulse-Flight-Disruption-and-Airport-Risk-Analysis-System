import numpy as np


class DelayAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def analyze(self):

        # Eksik varış gecikmelerini analize dahil etmiyoruz
        delays = self.df["arr_delay"].dropna().to_numpy()

        results = {
            "average_delay": np.mean(delays),
            "median_delay": np.median(delays),
            "std_delay": np.std(delays),

            "75th_percentile": np.percentile(delays, 75),
            "90th_percentile": np.percentile(delays, 90),
            "95th_percentile": np.percentile(delays, 95),

            "delay_15_rate": np.mean(delays >= 15) * 100,
            "delay_30_rate": np.mean(delays >= 30) * 100,
            "delay_60_rate": np.mean(delays >= 60) * 100,
            "delay_120_rate": np.mean(delays >= 120) * 100
        }

        return results


    def hourly_analysis(self):

        hourly = self.df[
            self.df["departure_hour"].between(5, 23)
        ].groupby("departure_hour").agg(
            total_flights=("departure_hour", "size"),
            average_delay=("arr_delay", "mean")
            )

        delayed_15 = (
         self.df["arr_delay"] >= 15
        ).groupby(
         self.df["departure_hour"]
        ).mean() * 100

        hourly["delay_15_rate"] = delayed_15

        return hourly

    def weekday_analysis(self):

        weekday = self.df.groupby("day_of_week").agg(
            total_flights=("day_of_week", "size"),
            average_delay=("arr_delay", "mean"),
            median_delay=("arr_delay", "median"),
            std_delay=("arr_delay", "std"),
            cancellation_rate=("cancelled", "mean")
        )

        delay_15 = (
            self.df["arr_delay"] >= 15
        ).groupby(
            self.df["day_of_week"]
        ).mean() * 100

        weekday["delay_15_rate"] = delay_15
        weekday["cancellation_rate"] *= 100

        return weekday

    def monthly_analysis(self):

        monthly = self.df.groupby("month").agg(
            total_flights=("month", "size"),
            average_delay=("arr_delay", "mean"),
            cancellation_rate=("cancelled", "mean")
        )

        severe_delay = (
            self.df["arr_delay"] >= 60
        ).groupby(
            self.df["month"]
        ).mean() * 100

        monthly["severe_delay_rate"] = severe_delay
        monthly["cancellation_rate"] *= 100

        return monthly


    def delay_reason_analysis(self):

        reason_columns = [
            "carrier_delay",
            "weather_delay",
            "nas_delay",
            "security_delay",
            "late_aircraft_delay"
        ]

        totals = self.df[reason_columns].sum()

        percentages = (
            totals / totals.sum()
        ) * 100

        results = {
            "total_delay_minutes": totals,
            "percentage": percentages
        }

        return results