import os
import requests
import json

def fetch_monthly_data(username, year, month):
    # Create the directory structure
    directory = f"monthly_data/{username}/{year}"
    filename = f"{directory}/{year}{month:02}.json"

    # Create directories if they don't exist
    os.makedirs(directory, exist_ok=True)

    # Check if the file already exists
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Loaded data from {filename}")
    else:
        # Build the URL for the API request
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

# Example usage
data = fetch_monthly_data("generalzod", 2024, 8)
