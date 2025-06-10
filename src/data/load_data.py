def load_data(file_path):
    """
    Load the raw survey data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    import pandas as pd

    # Load the data
    data = pd.read_csv(file_path)

    return data