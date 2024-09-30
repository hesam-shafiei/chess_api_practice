import os
import requests
import json
from datetime import datetime



def fetch_monthly_data(username, year, month):

    current_year = datetime.now().year
    current_month = datetime.now().month

    if year > current_year or (year == current_year and month > current_month):
        raise ValueError("Can not request data for a future date")

    # Create the directory structure
    directory = f"monthly_data/{username}/{year}"
    filename = f"{directory}/{year}{month:02}.json"

    if year == current_year and month == current_month:
        print("getting liva data for current month...")
        url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month:02}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
        }

        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful

        # Parse the JSON response
        data = response.json()
        return data


    # Create directories if they don't exist
    os.makedirs(directory, exist_ok=True)

    # Check if the file already exists
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Loaded data from {filename}")
    else:
        # Build the URL for the API request
        #https://api.chess.com/pub/player/thepizzaguy99/games/2023/03
        #https://api.chess.com/pub/player/thepizzaguy99/games/archives
        url = f"https://api.chess.com/pub/player/{username}/games/{year}/{month:02}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3 MyApp/1.0 (hesamshafiei7@gmail.com)"
        }

        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Ensure the request was successful

        # Parse the JSON response
        data = response.json()

        # Save the data locally
        with open(filename, 'w') as file:
            json.dump(data, file)
            print(f"Saved data to {filename}")

    return data


