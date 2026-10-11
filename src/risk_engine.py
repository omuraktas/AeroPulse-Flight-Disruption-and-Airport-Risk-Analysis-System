import numpy as np


class RiskEngine:

    def __init__(self):
        pass

    def airport_reliability_score(self, airport_results):

        results = airport_results.copy()

        # Ortalama gecikmeyi 0-100 skora çevir
        # 0 dakika veya daha iyi = 100 puan
        # 60+ dakika = 0 puan
        delay_score = (
            100 - (
                results["average_delay"].clip(0, 60)
                / 60 * 100
            )
        )

        results["reliability_score"] = (
            results["on_time_rate"] * 0.40
            + (100 - results["severe_delay_rate"]) * 0.25
            + (100 - results["cancellation_rate"]) * 0.20
            + delay_score * 0.10
            + (100 - results["diversion_rate"]) * 0.05
        )

        results["reliability_score"] = (
            results["reliability_score"].round(2)
        )

        return results

    def airline_reliability_score(self, airline_results):

        results = airline_results.copy()

        delay_score = (
            100 - (
                results["average_delay"].clip(0, 60)
                / 60 * 100
            )
        )

        results["reliability_score"] = (
            results["on_time_rate"] * 0.40
            + (100 - results["severe_delay_rate"]) * 0.25
            + (100 - results["cancellation_rate"]) * 0.20
            + delay_score * 0.10
            + (100 - results["diversion_rate"]) * 0.05
        )

        results["reliability_score"] = (
            results["reliability_score"].round(2)
        )

        return results

    def route_risk_score(self, route_results):

        results = route_results.copy()

        # Ortalama gecikme skoru
        delay_score = (
            results["average_delay"]
            .clip(0, 60)
            / 60 * 100
        )

        # Gecikme değişkenliği
        variation_score = (
            results["delay_std"]
            .clip(0, 100)
            / 100 * 100
        )

        # Rota yoğunluğu
        volume_score = (
            results["total_flights"]
            / results["total_flights"].max()
            * 100
        )

        # Risk skoru
        results["risk_score"] = (
            delay_score * 0.25
            + results["severe_delay_rate"] * 0.30
            + results["cancellation_rate"] * 0.20
            + variation_score * 0.15
            + volume_score * 0.10
        )

        results["risk_score"] = (
            results["risk_score"]
            .clip(0, 100)
            .round(2)
        )

        # Risk seviyeleri
        conditions = [
            results["risk_score"] <= 20,
            results["risk_score"] <= 40,
            results["risk_score"] <= 60,
            results["risk_score"] <= 80
        ]

        levels = [
            "LOW",
            "MODERATE",
            "HIGH",
            "VERY HIGH"
        ]

        results["risk_level"] = np.select(
            conditions,
            levels,
            default="CRITICAL"
        )

        return results