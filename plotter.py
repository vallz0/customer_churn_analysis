import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, data):
        self.data = data

    def create_histograms(self, color_column: str):
        unique_values = self.data[color_column].unique()

        for column in self.data.columns:
            if column != color_column:
                plt.figure(figsize=(8, 6))
                for value in unique_values:
                    subset = self.data[self.data[color_column] == value]
                    plt.hist(
                        subset[column],
                        alpha=0.7,
                        bins=15,
                        label=f"{color_column}={value}",
                    )

                plt.title(f"Distribution of {column} by {color_column}")
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.legend()
                plt.grid(True)
                plt.tight_layout()
                plt.show()
