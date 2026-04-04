import requests

keyword = input("Enter your keyword: ").strip()
url = "https://api.tvmaze.com/search/shows"

try:
	response = requests.get(url, params={"q": keyword}, timeout=10)
	response.raise_for_status()
	data = response.json()
	print(data)
except requests.exceptions.RequestException as exc:
	print(f"Request failed: {exc}")
except ValueError:
	print("The server response was not valid JSON.")