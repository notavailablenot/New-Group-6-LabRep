from hoopstatsview import HoopStatsView
import pandas as pd

def cleanStats(dataframe):
    for column in ['FG', '3PT', 'FT']:
        makes_attempts = dataframe[column].str.split('-', expand=True)
        makes_attempts.columns = [f"{column}M", f"{column}A"]
        dataframe = pd.concat([dataframe, makes_attempts], axis=1)
        dataframe.drop(column, axis=1, inplace=True)
    return dataframe

def main():
    """Loads the data frame, cleans it, prints it, creates the view, and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    cleaned_frame = cleanStats(frame)
    print("Cleaned DataFrame:")
    print(cleaned_frame)
    HoopStatsView(cleaned_frame)

if __name__ == "__main__":
    main()
