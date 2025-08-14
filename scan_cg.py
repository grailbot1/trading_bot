import requests
import pandas as pd
from datetime import datetime

def fetch_top_gainers():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    data = response.json().get("coins", [])
    rows = []
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    for c in data:
        item = c["item"]
        rows.append({
            "timestamp": timestamp,
            "symbol": item.get("symbol", ""),
            "name": item.get("name", ""),
        })
    df = pd.DataFrame(rows)
    df.to_csv("data/cg_gainers.csv", index=False)

if __name__ == "__main__":
    fetch_top_gainers()
    print("Scan complete")
