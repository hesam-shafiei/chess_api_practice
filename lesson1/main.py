import requests

#What is API?
#API lets us use data from other applications in our application
#how do we that? by making REQUESTS to the API (thats why we imported requests)


username = "chess_hesam"
url = f"https://api.chess.com/pub/player/{username}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers = headers)

print("Status Code:", response.status_code)

player_data = response.json()
print("Username: " + player_data["username"])

