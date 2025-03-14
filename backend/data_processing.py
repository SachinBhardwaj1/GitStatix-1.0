import pandas as pd

def process_data(file_path="data/github_issues_data.csv"):
    """Load and clean GitHub issues data."""
    df = pd.read_csv(file_path)

    # Convert timestamps to datetime
    df["created_at"] = pd.to_datetime(df["created_at"])
    df["closed_at"] = pd.to_datetime(df["closed_at"], errors='coerce')

    # Compute resolution time in hours
    df["resolution_time"] = (df["closed_at"] - df["created_at"]).dt.total_seconds() / 3600  # in hours

    # Save cleaned data
    df.to_csv("data/cleaned_github_issues_data.csv", index=False)
    print("Data cleaned and saved to data/cleaned_github_issues_data.csv")

if __name__ == "__main__":
    process_data()