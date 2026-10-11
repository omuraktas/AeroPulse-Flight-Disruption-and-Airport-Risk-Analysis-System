class RouteAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def analyze(self, min_flights=20):

        # JFK → LAX gibi rota oluştur
        self.df["route"] = (
            self.df["origin"]
            + " -> "
            + self.df["dest"]
        )

        # 60+ dakika gecikme
        self.df["severe_delay"] = (
            self.df["arr_delay"] >= 60
        )

        results = self.df.groupby("route").agg(
            total_flights=("route", "size"),
            average_delay=("arr_delay", "mean"),
            delay_std=("arr_delay", "std"),
            severe_delay_rate=("severe_delay", "mean"),
            cancellation_rate=("cancelled", "mean")
    )

        results["severe_delay_rate"] *= 100
        results["cancellation_rate"] *= 100

        # Çok az uçuşu olan rotaları çıkar
        results = results[
            results["total_flights"] >= min_flights
        ]

        return results