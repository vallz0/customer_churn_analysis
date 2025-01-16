from data_loader import DataLoader
from plotter import Plotter
from config import FILE_PATH, COLOR_COLUMN

def main():
    file_path = FILE_PATH
    color_column = COLOR_COLUMN

    data_loader = DataLoader(file_path)
    data = data_loader.load_and_clean_data()

    summary = data_loader.get_summary(color_column)
    print("Summary of the 'cancelled' column:")
    print(summary)

    plotter = Plotter(data)
    plotter.create_histograms(color_column=color_column)


if __name__ == "__main__":
    main()
