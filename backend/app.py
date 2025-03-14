import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load processed data
df = pd.read_csv("data/cleaned_github_issues_data.csv")

# Aggregate issue counts per repo
repo_issue_counts = df["repo"].value_counts().reset_index()
repo_issue_counts.columns = ["Repository", "Issue Count"]

# Create a time-series plot of issue trends
df["created_at"] = pd.to_datetime(df["created_at"])
issues_per_month = df.resample("ME", on="created_at").size().reset_index(name="Issue Count")

fig_trend = px.line(issues_per_month, x="created_at", y="Issue Count",
                     title="GitHub Issues Over Time")

# Initialize Dash App
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("GitHub Repo Insights Dashboard", style={'text-align': 'center'}),

    # Repository-wise Issue Count
    dcc.Graph(
        figure=px.bar(repo_issue_counts, x="Repository", y="Issue Count",
                      title="Issue Counts by Repository", color="Issue Count")
    ),

    # Time-Series Trend of Issues
    dcc.Graph(figure=fig_trend),

    # Forecasting Plot
    html.Img(src="assets/forecasting_plot.png", style={'width': '100%'})
])

if __name__ == "__main__":
    app.run_server(debug=True)
