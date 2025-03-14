import os
import requests
import pandas as pd
from datetime import datetime, timedelta, UTC
from dotenv import load_dotenv

# Load GitHub API Token
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# Repositories to track
REPOSITORIES = [
    "hwchase17/langchain",
    "microsoft/autogen",
    "stutipandey20/MyDSAPractice",
    "openai/openai-cookbook",
    "elastic/elasticsearch"
]

def fetch_github_events(repo, event_type):
    """Fetch GitHub events like pushes, PRs, merges."""
    url = f"https://api.github.com/repos/{repo}/events?per_page=100"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        events = response.json()
        filtered_events = [e for e in events if e["type"] == event_type]
        return [(repo, e) for e in filtered_events]
    else:
        print(f"⚠️ Failed to fetch {event_type} for {repo}: {response.status_code}")
        return []

def fetch_all_events():
    """Fetch PRs, Pushes, and Merges."""
    all_events = []
    for repo in REPOSITORIES:
        all_events.extend(fetch_github_events(repo, "PushEvent"))
        all_events.extend(fetch_github_events(repo, "PullRequestEvent"))

    return all_events

def save_to_csv(data):
    """Save event data to CSV."""
    df = pd.DataFrame([{**event[1], "repo": event[0]} for event in data])
    df.to_csv("data/github_events_data.csv", index=False)
    print("✅ Data saved to data/github_events_data.csv")

if __name__ == "__main__":
    print("📡 Fetching GitHub activity data...")
    events_data = fetch_all_events()
    save_to_csv(events_data)
