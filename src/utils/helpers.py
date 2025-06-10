import pandas as pd

def save_to_csv(data, filename):
    """Saves a DataFrame to a CSV file."""
    data.to_csv(filename, index=False)

def load_from_csv(filename):
    """Loads data from a CSV file into a DataFrame."""
    return pd.read_csv(filename)