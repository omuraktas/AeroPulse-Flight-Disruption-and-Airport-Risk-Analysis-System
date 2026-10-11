class SearchEngine:

    def __init__(self, dataframe, airport_scores, route_scores):
        self.df = dataframe
        self.airport_scores = airport_scores
        self.route_scores = route_scores

    def search_airport(self, airport_code):

        airport_code = airport_code.upper()

        if airport_code not in self.airport_scores.index:
            print("\nHavalimani bulunamadi.")
            return

        airport = self.airport_scores.loc[airport_code]

        print(f"\n--- {airport_code} AIRPORT ---")

        print(f"Toplam Ucus: {airport['total_flights']:.0f}")
        print(f"Ortalama Gecikme: {airport['average_delay']:.2f} dakika")
        print(f"Zamaninda Ucus Orani: %{airport['on_time_rate']:.2f}")
        print(f"Iptal Orani: %{airport['cancellation_rate']:.2f}")
        print(f"Reliability Score: {airport['reliability_score']:.2f}")

        airport_routes = self.route_scores[
            self.route_scores.index.str.startswith(
                airport_code + " ->"
            )
        ]

        airport_routes = airport_routes.sort_values(
            "risk_score",
            ascending=False
        ).head(5)

        print("\nEn Problemli Rotalar:")

        if airport_routes.empty:
            print("Yeterli rota verisi yok.")
        else:
            print(
                airport_routes[
                    [
                        "total_flights",
                        "average_delay",
                        "risk_score",
                        "risk_level"
                    ]
                ]
            )

    
    
    def compare_airports(self, airport1, airport2):

        airport1 = airport1.upper()
        airport2 = airport2.upper()

        if airport1 not in self.airport_scores.index:
            print(f"\n{airport1} bulunamadi.")
            return

        if airport2 not in self.airport_scores.index:
            print(f"\n{airport2} bulunamadi.")
            return

        first = self.airport_scores.loc[airport1]
        second = self.airport_scores.loc[airport2]

        print(f"\n--- {airport1} vs {airport2} ---")

        print(
            f"\n{airport1}"
            f"\nToplam Ucus: {first['total_flights']:.0f}"
            f"\nOrtalama Gecikme: {first['average_delay']:.2f} dk"
            f"\nZamaninda Ucus: %{first['on_time_rate']:.2f}"
            f"\nIptal Orani: %{first['cancellation_rate']:.2f}"
            f"\nReliability Score: {first['reliability_score']:.2f}"
        )

        print(
            f"\n\n{airport2}"
            f"\nToplam Ucus: {second['total_flights']:.0f}"
            f"\nOrtalama Gecikme: {second['average_delay']:.2f} dk"
            f"\nZamaninda Ucus: %{second['on_time_rate']:.2f}"
            f"\nIptal Orani: %{second['cancellation_rate']:.2f}"
            f"\nReliability Score: {second['reliability_score']:.2f}"
        )

        if first["reliability_score"] > second["reliability_score"]:

            print(
                f"\n\nSonuc: {airport1} operasyonel olarak daha guvenilir."
            )

        elif second["reliability_score"] > first["reliability_score"]:

            print(
                f"\n\nSonuc: {airport2} operasyonel olarak daha guvenilir."
            )

        else:

            print(
                "\n\nSonuc: Iki havalimaninin reliability score'u esit."
            )

    def compare_airlines(self, airline1, airline2, airline_scores):

        airline1 = airline1.upper()
        airline2 = airline2.upper()

        if airline1 not in airline_scores.index:
            print(f"\n{airline1} bulunamadi.")
            return

        if airline2 not in airline_scores.index:
            print(f"\n{airline2} bulunamadi.")
            return

        first = airline_scores.loc[airline1]
        second = airline_scores.loc[airline2]

        print(f"\n--- {airline1} vs {airline2} ---")

        print(
            f"\n{airline1}"
            f"\nToplam Ucus: {first['total_flights']:.0f}"
            f"\nOrtalama Gecikme: {first['average_delay']:.2f} dk"
            f"\nZamaninda Ucus: %{first['on_time_rate']:.2f}"
            f"\nIptal Orani: %{first['cancellation_rate']:.2f}"
            f"\nReliability Score: {first['reliability_score']:.2f}"
        )

        print(
            f"\n\n{airline2}"
            f"\nToplam Ucus: {second['total_flights']:.0f}"
            f"\nOrtalama Gecikme: {second['average_delay']:.2f} dk"
            f"\nZamaninda Ucus: %{second['on_time_rate']:.2f}"
            f"\nIptal Orani: %{second['cancellation_rate']:.2f}"
            f"\nReliability Score: {second['reliability_score']:.2f}"
        )

        if first["reliability_score"] > second["reliability_score"]:
            print(
                f"\n\nSonuc: {airline1} operasyonel olarak daha guvenilir."
            )

        elif second["reliability_score"] > first["reliability_score"]:
            print(
                f"\n\nSonuc: {airline2} operasyonel olarak daha guvenilir."
            )

        else:
            print(
                "\n\nSonuc: Iki havayolunun reliability score'u esit."
            )
