import time

from src.data_loader import FlightDataLoader


file_path = "data/flight_data_2024.csv"

loader = FlightDataLoader(file_path)

ROW_COUNT = 1000000


# Normal yükleme
start = time.perf_counter()

df = loader.load_data(
    nrows=ROW_COUNT
)

normal_time = time.perf_counter() - start


# Optimize yükleme
start = time.perf_counter()

df = loader.load_optimized(
    nrows=ROW_COUNT,
    usecols=[
        "op_unique_carrier",
        "origin",
        "dest",
        "dep_delay",
        "arr_delay",
        "cancelled",
        "diverted",
        "distance"
    ]
)

optimized_time = time.perf_counter() - start


print(f"Normal sure: {normal_time:.2f} saniye")
print(f"Optimize sure: {optimized_time:.2f} saniye")