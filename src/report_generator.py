import os


class ReportGenerator:

    def __init__(self, output_folder="outputs/reports"):
        self.output_folder = output_folder

        os.makedirs(
            self.output_folder,
            exist_ok=True
        )

    def generate_reports(
        self,
        airport_scores,
        airline_scores,
        route_scores,
        anomalies
    ):

        airport_scores.to_csv(
            f"{self.output_folder}/airport_rankings.csv"
        )

        airline_scores.to_csv(
            f"{self.output_folder}/airline_rankings.csv"
        )

        high_risk_routes = route_scores[
            route_scores["risk_score"] >= 40
        ]

        high_risk_routes.to_csv(
            f"{self.output_folder}/high_risk_routes.csv"
        )

        anomalies.to_csv(
            f"{self.output_folder}/anomalies.csv"
        )

        print(
            "\nRaporlar outputs/reports klasorune kaydedildi."
        )