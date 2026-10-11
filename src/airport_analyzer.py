class AirportAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def analyze(self, min_flights=50):

        results = self.df.groupby("origin").agg(
            total_flights=("origin", "size"),
            average_delay=("dep_delay", "mean"),
            cancellation_rate=("cancelled", "mean"),
            diversion_rate=("diverted", "mean")
        )

        results["on_time_rate"] = (
            self.df["dep_delay"] <= 15
        ).groupby(
            self.df["origin"]
        ).mean()

        results["severe_delay_rate"] = (
            self.df["dep_delay"] >= 60
        ).groupby(
            self.df["origin"]
        ).mean()

        results["cancellation_rate"] *= 100
        results["diversion_rate"] *= 100
        results["on_time_rate"] *= 100
        results["severe_delay_rate"] *= 100

        results = results[
            results["total_flights"] >= min_flights
        ]

        return results