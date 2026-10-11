import matplotlib.pyplot as plt

from src.data_loader import FlightDataLoader
from src.data_cleaner import DataCleaner
from src.feature_engineer import FeatureEngineer
from src.delay_analyzer import DelayAnalyzer
from src.airline_analyzer import AirlineAnalyzer
from src.airport_analyzer import AirportAnalyzer
from src.route_analyzer import RouteAnalyzer
from src.risk_engine import RiskEngine
from src.anomaly_detector import AnomalyDetector
from src.search_engine import SearchEngine
from src.visualizer import Visualizer
from src.menu import Menu
from src.report_generator import ReportGenerator


file_path = "data/flight_data_2024.csv"

loader = FlightDataLoader(file_path)

df = loader.load_data(nrows=200000)


# DATA CLEANING
cleaner = DataCleaner(df)
df = cleaner.clean()


# FEATURE ENGINEERING
feature_engineer = FeatureEngineer(df)
df = feature_engineer.create_features()


print(
    df[
        [
            "crs_dep_time",
            "departure_hour",
            "time_of_day",
            "is_weekend",
            "distance_category",
            "delay_category",
            "is_problematic"
        ]
    ].head(10)
)


# DELAY ANALYSIS
delay_analyzer = DelayAnalyzer(df)

delay_results = delay_analyzer.analyze()

print("\n--- DELAY ANALYSIS ---")

for key, value in delay_results.items():
    print(f"{key}: {value:.2f}")


# AIRLINE ANALYSIS
airline_analyzer = AirlineAnalyzer(df)

airline_results = airline_analyzer.analyze()

print("\n--- AIRLINE ANALYSIS ---")
print(airline_results)


best_airlines = airline_results.sort_values(
    "on_time_rate",
    ascending=False
).head(5)

worst_airlines = airline_results.sort_values(
    "on_time_rate",
    ascending=True
).head(5)


print("\n--- EN IYI 5 HAVAYOLU ---")

print(
    best_airlines[
        [
            "total_flights",
            "average_delay",
            "on_time_rate"
        ]
    ]
)


print("\n--- EN KOTU 5 HAVAYOLU ---")

print(
    worst_airlines[
        [
            "total_flights",
            "average_delay",
            "on_time_rate"
        ]
    ]
)


# AIRPORT ANALYSIS
airport_analyzer = AirportAnalyzer(df)

airport_results = airport_analyzer.analyze(
    min_flights=50
)

print("\n--- AIRPORT ANALYSIS ---")
print(airport_results)


print("\n--- EN YUKSEK GECIKME ORANINA SAHIP HAVALIMANLARI ---")

print(
    airport_results.sort_values(
        "on_time_rate",
        ascending=True
    ).head(10)
)


# ROUTE ANALYSIS
route_analyzer = RouteAnalyzer(df)

route_results = route_analyzer.analyze(
    min_flights=20
)

print("\n--- ROUTE ANALYSIS ---")
print(route_results)


print("\n--- EN PROBLEMLI YOGUN ROTALAR ---")

print(
    route_results.sort_values(
        "severe_delay_rate",
        ascending=False
    ).head(10)
)


# HOURLY ANALYSIS
hourly_results = delay_analyzer.hourly_analysis()

print("\n--- HOURLY DELAY ANALYSIS ---")
print(hourly_results)


hourly_results["average_delay"].plot(
    kind="line",
    marker="o"
)

plt.title("Average Delay by Departure Hour")
plt.xlabel("Departure Hour")
plt.ylabel("Average Arrival Delay (minutes)")
plt.grid()

plt.show()


# WEEKDAY ANALYSIS
weekday_results = delay_analyzer.weekday_analysis()

print("\n--- WEEKDAY DELAY ANALYSIS ---")
print(weekday_results)


# MONTHLY ANALYSIS - FULL DATASET
monthly_df = loader.load_data(
    usecols=[
        "month",
        "arr_delay",
        "cancelled"
    ]
)

monthly_analyzer = DelayAnalyzer(
    monthly_df
)

monthly_results = monthly_analyzer.monthly_analysis()

print("\n--- MONTHLY ANALYSIS ---")
print(monthly_results)


# DELAY REASON ANALYSIS
delay_reason_df = loader.load_data(
    usecols=[
        "carrier_delay",
        "weather_delay",
        "nas_delay",
        "security_delay",
        "late_aircraft_delay"
    ]
)

delay_reason_analyzer = DelayAnalyzer(
    delay_reason_df
)

delay_reason_results = (
    delay_reason_analyzer.delay_reason_analysis()
)


print("\n--- DELAY REASONS ---")

print("\nToplam gecikme dakikalari:")

print(
    delay_reason_results[
        "total_delay_minutes"
    ]
)


print("\nGecikmeye katkisi (%):")

print(
    delay_reason_results[
        "percentage"
    ]
)


# RISK ENGINE
risk_engine = RiskEngine()


# AIRPORT RELIABILITY
airport_scores = (
    risk_engine.airport_reliability_score(
        airport_results
    )
)

print("\n--- AIRPORT RELIABILITY SCORES ---")

print(
    airport_scores.sort_values(
        "reliability_score",
        ascending=False
    )[
        [
            "total_flights",
            "average_delay",
            "on_time_rate",
            "reliability_score"
        ]
    ].head(10)
)


# AIRLINE RELIABILITY
airline_scores = (
    risk_engine.airline_reliability_score(
        airline_results
    )
)

print("\n--- AIRLINE RELIABILITY SCORES ---")

print(
    airline_scores.sort_values(
        "reliability_score",
        ascending=False
    )[
        [
            "total_flights",
            "average_delay",
            "on_time_rate",
            "reliability_score"
        ]
    ]
)


# ROUTE RISK
route_scores = (
    risk_engine.route_risk_score(
        route_results
    )
)

print("\n--- ROUTE RISK SCORES ---")

print(
    route_scores.sort_values(
        "risk_score",
        ascending=False
    )[
        [
            "total_flights",
            "average_delay",
            "severe_delay_rate",
            "cancellation_rate",
            "delay_std",
            "risk_score",
            "risk_level"
        ]
    ].head(10)
)


# SEARCH ENGINE
search_engine = SearchEngine(
    df,
    airport_scores,
    route_scores
)


# ANOMALY DETECTION
anomaly_detector = AnomalyDetector(df)

anomalies = (
    anomaly_detector.detect_daily_anomalies()
)

print("\n--- DAILY ANOMALIES ---")
print(anomalies.head(10))


# WORST DAY INVESTIGATION
if not anomalies.empty:

    worst_day = anomalies.index[0]

    airlines, airports, hours, routes = (
        anomaly_detector.investigate_day(
            worst_day
        )
    )

    print("\n--- EN PROBLEMLI GUN ---")
    print(worst_day)

    print("\n--- EN COK ETKILENEN HAVAYOLLARI ---")
    print(airlines.head(5))

    print("\n--- EN COK ETKILENEN HAVALIMANLARI ---")
    print(airports.head(5))

    print("\n--- EN PROBLEMLI SAATLER ---")
    print(hours.head(5))

    print("\n--- EN PROBLEMLI ROTALAR ---")
    print(routes.head(5))


# VISUALIZATION
visualizer = Visualizer()

visualizer.airline_reliability(
    airline_scores
)

visualizer.airport_reliability(
    airport_scores
)

visualizer.hourly_delay(
    hourly_results
)

visualizer.monthly_delay(
    monthly_results
)

visualizer.weekday_delay(
    weekday_results
)

visualizer.route_risk(
    route_scores
)

visualizer.delay_reasons(
    delay_reason_results
)

visualizer.anomaly_days(
    anomalies
)

print(
    "\nGrafikler outputs/charts klasorune kaydedildi."
)


# REPORT GENERATOR
report_generator = ReportGenerator()

report_generator.generate_reports(
    airport_scores,
    airline_scores,
    route_scores,
    anomalies
)


# TERMINAL MENU
menu = Menu()

while True:

    choice = menu.show()

    if choice == "1":

        print("\n--- AIRLINE ANALYSIS ---")
        print(airline_results)

    elif choice == "2":

        print("\n--- AIRPORT ANALYSIS ---")
        print(airport_results)

    elif choice == "3":

        print("\n--- ROUTE ANALYSIS ---")
        print(route_results)

    elif choice == "4":

        print("\n--- ROUTE RISK SCORES ---")

        print(
            route_scores.sort_values(
                "risk_score",
                ascending=False
            ).head(10)
        )

    elif choice == "5":

        print("\n--- ANOMALIES ---")
        print(anomalies)

    elif choice == "6":

        airport_code = input(
            "\nHavalimani kodu girin: "
        )

        search_engine.search_airport(
            airport_code
        )

    elif choice == "7":

        airport1 = input(
            "\nBirinci havalimani kodu: "
        )

        airport2 = input(
            "Ikinci havalimani kodu: "
        )

        search_engine.compare_airports(
            airport1,
            airport2
        )

    elif choice == "8":

        airline1 = input(
            "\nBirinci havayolu kodu: "
        )

        airline2 = input(
            "Ikinci havayolu kodu: "
        )

        search_engine.compare_airlines(
            airline1,
            airline2,
            airline_scores
        )

    elif choice == "9":

        print("\nAeroPulse kapatiliyor...")
        break

    else:

        print("\nGecersiz secim.")