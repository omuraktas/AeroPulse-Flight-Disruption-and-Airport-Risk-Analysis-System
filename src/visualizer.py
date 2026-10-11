import matplotlib.pyplot as plt
import os


class Visualizer:

    def __init__(self, output_folder="outputs/charts"):
        self.output_folder = output_folder

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    def airline_reliability(self, airline_scores):

        data = airline_scores.sort_values(
            "reliability_score",
            ascending=False
        )

        plt.figure(figsize=(10, 6))

        plt.bar(
            data.index,
            data["reliability_score"]
        )

        plt.title("Airline Reliability Scores")
        plt.xlabel("Airline")
        plt.ylabel("Reliability Score")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/airline_reliability.png"
        )

        plt.close()

    def airport_reliability(self, airport_scores):

        data = airport_scores.sort_values(
            "reliability_score",
            ascending=False
        ).head(15)

        plt.figure(figsize=(10, 6))

        plt.bar(
            data.index,
            data["reliability_score"]
        )

        plt.title("Top Airport Reliability Scores")
        plt.xlabel("Airport")
        plt.ylabel("Reliability Score")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/airport_reliability.png"
        )

        plt.close()

    def hourly_delay(self, hourly_results):

        plt.figure(figsize=(10, 6))

        plt.plot(
            hourly_results.index,
            hourly_results["average_delay"],
            marker="o"
        )

        plt.title("Average Delay by Departure Hour")
        plt.xlabel("Departure Hour")
        plt.ylabel("Average Delay (Minutes)")

        plt.grid()

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/hourly_delay.png"
        )

        plt.close()

    def monthly_delay(self, monthly_results):

        plt.figure(figsize=(10, 6))

        plt.plot(
            monthly_results.index,
            monthly_results["average_delay"],
            marker="o"
        )

        plt.title("Average Delay by Month")
        plt.xlabel("Month")
        plt.ylabel("Average Delay (Minutes)")

        plt.grid()

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/monthly_delay.png"
        )

        plt.close()

    def weekday_delay(self, weekday_results):

        plt.figure(figsize=(10, 6))

        plt.bar(
            weekday_results.index,
            weekday_results["average_delay"]
        )

        plt.title("Average Delay by Day of Week")
        plt.xlabel("Day of Week")
        plt.ylabel("Average Delay (Minutes)")

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/weekday_delay.png"
        )

        plt.close()

    def route_risk(self, route_scores):

        data = route_scores.sort_values(
            "risk_score",
            ascending=False
        ).head(10)

        plt.figure(figsize=(10, 6))

        plt.barh(
            data.index,
            data["risk_score"]
        )

        plt.title("Highest Risk Routes")
        plt.xlabel("Risk Score")
        plt.ylabel("Route")

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/route_risk.png"
        )

        plt.close()

    def delay_reasons(self, delay_reason_results):

        data = delay_reason_results["percentage"]

        plt.figure(figsize=(10, 6))

        plt.bar(
            data.index,
            data.values
        )

        plt.title("Delay Reason Distribution")
        plt.xlabel("Delay Reason")
        plt.ylabel("Percentage (%)")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/delay_reasons.png"
        )

        plt.close()

    def anomaly_days(self, anomalies):

        plt.figure(figsize=(10, 6))

        plt.bar(
            anomalies.index.astype(str),
            anomalies["average_delay"]
        )

        plt.title("Anomalous Operation Days")
        plt.xlabel("Date")
        plt.ylabel("Average Delay")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            f"{self.output_folder}/anomaly_days.png"
        )

        plt.close()