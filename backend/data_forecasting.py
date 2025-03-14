import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def forecast_arima(file_path="data/cleaned_github_issues_data.csv"):
    """Apply ARIMA model to forecast issue trends."""
    df = pd.read_csv(file_path)
    df["created_at"] = pd.to_datetime(df["created_at"])
    df.set_index("created_at", inplace=True)

    # Aggregate issues count by month
    issue_counts = df.resample("M").size()

    # Fit ARIMA model
    model = ARIMA(issue_counts, order=(5,1,0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=6)  # Predict next 6 months

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(issue_counts, label="Historical Data")
    plt.plot(forecast, label="Forecast", linestyle="dashed")
    plt.legend()
    plt.title("GitHub Issues Forecast")
    
    plt.savefig("results/forecasting_plot.png")
    print("Forecasting plot saved to results/forecasting_plot.png")

if __name__ == "__main__":
    forecast_arima()
