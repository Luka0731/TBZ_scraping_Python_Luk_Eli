import requests

api_key = "67d9426d3d477a41138f6406"
url = "https://api.scrapingdog.com/google/"
params = {
"api_key": api_key,
"query": "lead generation tools",
"results": 10,
"country": "us",
"page": 0
}
response = requests.get(url, params=params)
if response.status_code == 200:
  data = response.json()
  print(data)
else:
  print(f"Request failed with status code: {response.status_code}")