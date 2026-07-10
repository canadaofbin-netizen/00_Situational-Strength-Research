import sys
import requests
import json

# Semantic Scholar API Example
# Using the anonymous REST API endpoint for paper search

def search_semantic_scholar(query, limit=3):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,abstract,year,authors,citationCount"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print(f"Error searching Semantic Scholar: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_academic.py <search_query>")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    results = search_semantic_scholar(query)
    print(json.dumps(results, indent=2, ensure_ascii=False))
