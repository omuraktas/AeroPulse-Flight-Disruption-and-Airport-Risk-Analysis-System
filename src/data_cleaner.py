import pandas as pd


class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def clean(self):

        self.df = self.df.drop_duplicates()

        self.df["fl_date"] = pd.to_datetime(
            self.df["fl_date"]
        )

        return self.df