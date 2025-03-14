import os
import json
from flask import Flask, request, jsonify
from openai import OpenAI
from elasticsearch import Elasticsearch

# Load API keys
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
es = Elasticsearch("http://localhost:9200")

app = Flask(__name__)

def embed_text(text):
    """Generate OpenAI embeddings for a given text."""
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response["data"][0]["embedding"]

@app.route("/search", methods=["GET"])
def search_issues():
    """Search GitHub issues using semantic search."""
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    embedding = embed_text(query)
    
    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                "params": {"query_vector": embedding}
            }
        }
    }
    
    results = es.search(index="github_issues", body={"query": script_query}, size=5)
    return jsonify(results["hits"]["hits"])

if __name__ == "__main__":
    app.run(port=5001, debug=True)
