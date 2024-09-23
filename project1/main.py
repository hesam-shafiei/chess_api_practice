# main.py

import helper

def top_games_of_month(username, year, month):
    # Use the fetch_monthly_data function from helper.py
    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    wins = []

    for game in games:
        # If username is playing as white:
        if game["white"]["username"].lower() == username.lower():
            # If the result for white is a win:
            if game["white"]["result"] == "win":
                black_rating = game["black"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": black_rating
                }
                wins.append(new_game)

        # If username is playing as black:
        elif game["black"]["username"].lower() == username.lower():
            # If the result for black is a win:
            if game["black"]["result"] == "win":
                white_rating = game["white"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": white_rating
                }
                wins.append(new_game)
        
    # Sort the wins by opponent's rating in descending order
    wins = sorted(wins, key=lambda x: x["opp_rating"], reverse=True)

    # Select the top 10 wins
    top_10_wins = wins[:10]
    counter = 1
    for win in top_10_wins:
        game = win["game"]
        opp_rating = win["opp_rating"]
        url = game["url"]

        print(f"{counter}. url: {url}")
        print(f"opponent rating: {opp_rating}")
        print()
        counter += 1

def worst_games_of_month(username, year, month):
    # Use the fetch_monthly_data function from helper.py
    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    losses = []

    for game in games:
        # If username is playing as white:
        if game["white"]["username"].lower() == username.lower():
            # If the result for white is a loss:
            # if the result for black is a win
            if game["black"]["result"] == "win":
                black_rating = game["black"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": black_rating
                }
                losses.append(new_game)

        # If username is playing as black:
        elif game["black"]["username"].lower() == username.lower():
            # If the result for black is a loss:
            # if the result for white is a win:
            if game["white"]["result"] == "win":
                white_rating = game["white"]["rating"]
                new_game = {
                    "game": game,
                    "opp_rating": white_rating
                }
                losses.append(new_game)

    # Sort the losses by opponent's rating in accending order
    losses = sorted(losses, key=lambda x: x["opp_rating"], reverse=False)

    # Select the top 10 wins
    top_10_losses = losses[:10]
    counter = 1
    for loss in top_10_losses:
        game = loss["game"]
        opp_rating = loss["opp_rating"]
        url = game["url"]

        print(f"{counter}. url: {url}")
        print(f"opponent rating: {opp_rating}")
        print()
        counter += 1
# Example usage
worst_games_of_month("generalzod", 2024, 8)