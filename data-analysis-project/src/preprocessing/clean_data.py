import pandas as pd

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the dataset by handling missing values and normalizing data."""
    # Handle missing values
    df = df.dropna()  # Example: drop rows with missing values
    # Normalize data if necessary
    # df['column_name'] = (df['column_name'] - df['column_name'].mean()) / df['column_name'].std()  # Example normalization
    return df

def save_cleaned_data(df, output_path):
    """Save the cleaned dataset to a CSV file."""
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw_data_path = '../data/raw/parentalidade.csv'
    cleaned_data_path = '../data/processed/cleaned_data.csv'
    
    # Load raw data
    data = load_data(raw_data_path)
    
    # Clean data
    cleaned_data = clean_data(data)
    
    # Save cleaned data
    save_cleaned_data(cleaned_data, cleaned_data_path)