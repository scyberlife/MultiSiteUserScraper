<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/scyberlife/global-assets/blob/main/multi-site-username-scraper/multi-site-username-scraper.png">
 <source media="(prefers-color-scheme: light)" srcset="https://github.com/scyberlife/global-assets/blob/main/multi-site-username-scraper/multi-site-username-scraper.png">
 <img alt="YOUR-ALT-TEXT" src="YOUR-DEFAULT-IMAGE">
</picture>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Dancing+Script&weight=500&size=30&pause=1000&color=F7F7F7&center=true&vCenter=true&width=435&lines=++++++++++++++++++++++++++++++++++++Multi+Site+Username+Scraper)](https://git.io/typing-svg)

This is a Python script using Flask web framework and BeautifulSoup library to scrape various websites for a given username. It creates a dictionary of URLs where the username is present and saves the results to a JSON file. The script contains a Flask endpoint to handle search requests with a GET parameter for the username. The URL for each website to be searched is stored in a dictionary. If the username is present in the response, it is added to the search results dictionary. The results are returned as a JSON response.

## Requirements:

Before starting to work with the project, the following components must be installed:

- <a href="https://www.python.org/downloads/">Python</a>
- <a href="https://flask.palletsprojects.com/en/2.1.x/installation/">Flask</a>
- <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup</a>
- <a href="https://pypi.org/project/requests/">Requests</a>


## Installation:

Clone the repository to your local computer: 
```bash
git clone https://github.com/your_username/repository_name.git
```

Install all dependencies: 
```bash
pip install -r requirements.txt
```
## Usage:
Run the application:
```bash
python3 main.py
```
Then go to where 'USERNAME' is the username you want to find.:
```html
http://localhost:5000/search?username=<USERNAME>
```
The search results will be saved in JSON format in the search_results.json file.

## Examples of responses: 
 
```json
{
    "johndoe": [
        "https://github.com/johndoe",
        "https://www.tiktok.com/@johndoe",
        "https://pikabu.ru/@johndoe"
    ]
}
```

### Authors:

Sergei Beliaev - Idea and development - <a href="https://github.com/scyberlife">scyberlife</a>
