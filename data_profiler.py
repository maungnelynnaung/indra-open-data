import pandas as pd
import numpy as np
from ydata_profiling import ProfileReport

def main():
    """
    Main function to load and process the dataset.
    """
    csv_filename = "2024-08-26-kayin-saw-chit-thu-bdf-strength-dataset-v1.csv"
    try:
        df = pd.read_csv(csv_filename)
        print("DataFrame loaded successfully. Here's the head before wrangling:")
        print(df.head())

        # Data Wrangling Steps
        # 1. Remove duplicate rows
        df.drop_duplicates(inplace=True)
        print("\nRemoved duplicate rows.")

        # 2. Trim whitespace from string/object columns
        for col in df.select_dtypes(include=['object', 'string']).columns:
            df[col] = df[col].str.strip()
        print("\nTrimmed whitespace from string/object columns.")

        # 3. Replace empty strings with numpy.nan
        df.replace('', np.nan, inplace=True)
        print("\nReplaced empty strings with NaN.")

        # 4. Print data types
        print("\nData types of each column:")
        print(df.dtypes)

        # 5. Print summary analysis
        print("\nSummary analysis of the DataFrame:")
        print(df.describe(include='all'))

        # Generate Data Profile Report
        print("\nGenerating data profile report...")
        profile = ProfileReport(df, title="Data Profile Report")
        report_filename = "data_profile_report.html"
        profile.to_file(report_filename)
        print(f"Data profile report generated as {report_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
    except ImportError:
        print("Error: ydata_profiling library is not installed. Please install it using 'pip install ydata-profiling'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
