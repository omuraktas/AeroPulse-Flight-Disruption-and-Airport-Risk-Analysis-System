class AirlineAnalyzer:

    def __init__(self, dataframe):
        self.df = dataframe

    def analyze(self):

        results = self.df.groupby("op_unique_carrier").agg(
            total_flights=("op_unique_carrier", "size"),
            average_delay=("arr_delay", "mean"),
            cancellation_rate=("cancelled", "mean"),
            diversion_rate=("diverted", "mean")
        )

        results["on_time_rate"] = (
            self.df["arr_delay"] <= 15
        ).groupby(
            self.df["op_unique_carrier"]
        ).mean()

        results["severe_delay_rate"] = (
            self.df["arr_delay"] >= 60
        ).groupby(
            self.df["op_unique_carrier"]
        ).mean()

        results["cancellation_rate"] *= 100
        results["diversion_rate"] *= 100
        results["on_time_rate"] *= 100
        results["severe_delay_rate"] *= 100

        return results