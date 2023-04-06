from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from requests import get
from json import dump, dumps
from os import path


app = Flask(__name__)

# Directory to save the search results
dir_home = path.expanduser("~")
dir_file = path.join(dir_home, "Desktop", "search_results.json")

# Dictionary containing URLs to be searched
all_url = {
    "github": "https://github.com/",
    "career.habr": "https://career.habr.com/",
    "tiktok": "https://www.tiktok.com/@",
    "pikabu": "https://pikabu.ru/@",
    "reddit": "https://reddit.com/user/",
    "instagram": "https://instagram.com/",
}

# Endpoint to handle search requests
@app.route('/search')
def all_search():
    username = request.args.get('username')
    search_results = {}

    # Iterate over all URLs and check if the username is present in the response
    for url in all_url.values():
        try:
            response = get(url + username, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            user_info = soup.find('a', class_='_31VWB3vSkv19o3I7RVE710')
            user_info1 = soup.find('title')
        except:
            continue

        if username in str(user_info) or username in str(user_info1):
            if username not in search_results:
                search_results[username] = []
            search_results[username].append(f"{url}{username}")

    # Save the search results to a JSON file
    with open(dir_file, 'w') as f:
        dump(search_results, f, indent=4)

    # Return the search results as a JSON response
    return dumps(search_results, indent=2)

if __name__ == '__main__':
    app.run()