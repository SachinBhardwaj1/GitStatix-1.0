import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(file_path="data/cleaned_github_issues_data.csv"):
    """Generate visualizations of issue resolution time."""
    df = pd.read_csv(file_path)

    plt.figure(figsize=(12, 6))
    sns.histplot(df["resolution_time"].dropna(), bins=50, kde=True)
    plt.xlabel("Resolution Time (hours)")
    plt.ylabel("Number of Issues")
    plt.title("Distribution of Issue Resolution Times")
    
    plt.savefig("results/resolution_time_distribution.png")
    print("Visualization saved to results/resolution_time_distribution.png")

if __name__ == "__main__":
    visualize_data()