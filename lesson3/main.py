import requests
import json
import os

def fetch_monthly_data(url, username, date):

    folder = "chess_data"

    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = f"lesson3/{folder}/{username}_{date}.json"

    #if the json file already exists
    if os.path.exists(file_path):
        print("loading data from local computer")

        with open(file_path, "r") as file:
            data = json.load(file)

    else:
        #if it does not exist
        print("getting data from chess.com api")

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
        }

        response = requests.get(url, headers = headers)
        data = response.json()

        with open(file_path, "w") as file:
            json.dump(data, file)
    
    return data


url = "https://api.chess.com/pub/player/chess_hesam/games/2024/08"
username = "chess_hesam"
date = "202408"

fetch_monthly_data(url, username, date)