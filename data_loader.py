import pandas as pd


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def load_and_clean_data(self):
        self.data = pd.read_csv(self.file_path)
        self.data = self.data.drop(columns="CustomerID", errors="ignore")  # Remove CustomerID
        self.data = self.data.dropna()  # Remove rows with missing values
        return self.data

    def get_summary(self, column: str):
       return self.data[column].value_counts(normalize=True).map("{:.1%}".format)
