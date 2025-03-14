from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load event data
df = pd.read_csv("backend/data/github_events_data.csv")

@app.get("/activity")
def get_activity():
    """Returns Pull Requests, Pushes, Merges, and Merge Conflicts."""
    event_counts = df["type"].value_counts().to_dict()
    return event_counts

@app.get("/conflicts")
def get_conflicts():
    """Returns merge conflict issues."""
    conflict_issues = df[df["type"] == "PullRequestEvent"]
    return conflict_issues[["repo", "payload"]].to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
