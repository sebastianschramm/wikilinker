import requests


def get_wiki_summary(title: str):
    backup_response = "No details available"
    url = (
        f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts"
        f"&exsentences=5&exsectionformat=plain&explaintext=&titles={title}&format=json"
    )
    response = requests.get(url, headers={"Content-Type": "application/JSON"})
    if response.status_code == 200:
        try:
            response_obj = response.json()
            return "\n\n".join(
                [
                    f"Wikipedia page ID {key}:\n\n{item['extract']}"
                    for key, item in response_obj["query"]["pages"].items()
                ]
            )
        except Exception:
            return backup_response
    return backup_response
