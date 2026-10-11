import pandas as pd


class FlightDataLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self, nrows=None, usecols=None):
        df = pd.read_csv(
            self.file_path,
            nrows=nrows,
            usecols=usecols
        )

        return df

    def load_optimized(self, nrows=None, usecols=None):

        dtypes = {
            "year": "int16",
            "month": "int8",
            "day_of_month": "int8",
            "day_of_week": "int8",
            "op_unique_carrier": "category",
            "origin": "category",
            "dest": "category",
            "cancelled": "int8",
            "diverted": "int8",
            "dep_delay": "float32",
            "arr_delay": "float32",
            "distance": "float32"
        }

        if usecols is not None:
            dtypes = {
                column: dtype
                for column, dtype in dtypes.items()
                if column in usecols
            }

        df = pd.read_csv(
            self.file_path,
            nrows=nrows,
            usecols=usecols,
            dtype=dtypes
        )

        return df