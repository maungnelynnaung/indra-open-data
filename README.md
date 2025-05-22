# INDRA Innovation & Communication Open Data Repo

## Note to Users

As a jack-of-all-trades who loves working with data, information, and computers, I work on many random projects. Some people find some of my data/info products useful. Some want my datasets, high-quality images, etc. Therefore, I created this open-source data repository.

If you have ideas on how to make this information and data more useful and user-friendly, please feel free to let me know. Please feel free to contact me at <strong>[nelynnaung {at} indramyanmar.com]</strong> if you have any questions or need further information. However, I may not be able to immediately respond to every message as I need to do some part-time gigs for a living.

## File Naming Convention

I use the following format for naming files:

`YYYY-MM-DD filename.extension`

- `YYYY`: Four-digit year
- `MM`: Two-digit month
- `DD`: Two-digit day
- `filename`: Descriptive name of the file
- `extension`: File type extension (e.g., .txt, .jpg, .pdf)

---

## Data Profiler Script (`data_profiler.py`)

This Python script performs data loading, wrangling, and generates a profile report using Pandas and Y-Data Profiling.

**Input File:** `2024-08-26-kayin-saw-chit-thu-bdf-strength-dataset-v1.csv` (This file must be in the same directory as the script).

**Output Report:** `data_profile_report.html`

### Prerequisites

Before running the script, ensure you have Python installed. You will also need to install the required libraries.

### Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Install dependencies:**
    Navigate to the repository's root directory (where `requirements.txt` is located) and run:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Script

1.  Ensure the input CSV file (`2024-08-26-kayin-saw-chit-thu-bdf-strength-dataset-v1.csv`) is in the root directory of the repository.
2.  Execute the script from the root directory:
    ```bash
    python data_profiler.py
    ```
3.  Upon successful execution, the script will:
    *   Print the data types of the columns in the console.
    *   Print a summary description of the data in the console.
    *   Generate a detailed HTML data profile report named `data_profile_report.html` in the root directory.

The script includes error handling for cases where the input file is not found or if `ydata-profiling` is not installed correctly.