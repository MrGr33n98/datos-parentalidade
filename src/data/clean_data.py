import pandas as pd

def clean_data(file_path):
    # Load the raw data
    data = pd.read_csv(file_path)

    # Remove rows with missing values
    data_cleaned = data.dropna()

    # Remove duplicates
    data_cleaned = data_cleaned.drop_duplicates()

    # Additional cleaning steps can be added here

    return data_cleaned