# datos-parentalidade

This project is focused on analyzing parentality-related survey data. The dataset contains responses from individuals regarding their experiences and perceptions related to parentality in the workplace.

## Project Structure

- **data/**: Contains the datasets used in the analysis.
  - **raw/**: Contains the raw survey data collected for analysis.
    - `survey_data.csv`: The raw survey data.
  - **processed/**: Intended to store processed data files after cleaning and transformation.

- **notebooks/**: Contains Jupyter notebooks for data analysis.
  - `data_analysis.ipynb`: This notebook includes data exploration, visualization, and insights derived from the survey data.

- **src/**: Contains the source code for data processing and visualization.
  - **data/**: Contains scripts for data handling.
    - `clean_data.py`: Exports a function `clean_data()` to clean the raw data.
    - `load_data.py`: Exports a function `load_data()` to load the raw data from the CSV file.
  - **visualization/**: Contains scripts for creating visualizations.
    - `plots.py`: Exports functions for various visualizations, such as `plot_histogram()` and `plot_correlation_matrix()`.
  - **utils/**: Contains utility functions for common tasks.
    - `helpers.py`: Exports utility functions like `save_to_csv()` and `load_from_csv()`.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/MrGr33n98/datos-parentalidade.git
   ```

2. Navigate to the project directory:
   ```
   cd datos-parentalidade
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

- To clean the data, run the `clean_data()` function from `src/data/clean_data.py`.
- To load the data, use the `load_data()` function from `src/data/load_data.py`.
- For visualizations, utilize the functions in `src/visualization/plots.py`.
- Explore the analysis in the Jupyter notebook located in `notebooks/data_analysis.ipynb`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.