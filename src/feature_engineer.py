import numpy as np


class FeatureEngineer:

    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def create_features(self):

        # Kalkış saati
        self.df["departure_hour"] = (
            self.df["crs_dep_time"] // 100
        )

        # Günün bölümü
        conditions = [
            self.df["departure_hour"].between(5, 11),
            self.df["departure_hour"].between(12, 16),
            self.df["departure_hour"].between(17, 21)
        ]

        choices = [
            "MORNING",
            "AFTERNOON",
            "EVENING"
        ]

        self.df["time_of_day"] = np.select(
            conditions,
            choices,
            default="NIGHT"
        )

        # Hafta sonu mu?
        self.df["is_weekend"] = (
            self.df["day_of_week"].isin([6, 7])
        )

        # Mesafe kategorisi
        self.df["distance_category"] = np.select(
            [
                self.df["distance"] < 500,
                self.df["distance"].between(500, 1500)
            ],
            [
                "SHORT",
                "MEDIUM"
            ],
            default="LONG"
        )

        # Gecikme kategorisi
        self.df["delay_category"] = np.select(
            [
                self.df["arr_delay"] <= 15,
                self.df["arr_delay"].between(16, 60)
            ],
            [
                "ON_TIME",
                "DELAYED"
            ],
            default="SEVERE_DELAY"
        )

        # Problemli uçuş
        self.df["is_problematic"] = (
            (self.df["arr_delay"] > 15)
            | (self.df["cancelled"] == 1)
            | (self.df["diverted"] == 1)
        )

        return self.df