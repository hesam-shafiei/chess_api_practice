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


#make a function called: longest_win_streak
#it takes: username, year, and month as input
#prints: How many games was your highest win streak of that month
#prints: display every game in the win streak

def longest_win_streak(username, year, month):

    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    longest_streak = 0
    current_streak = 0
    streak_games = []
    current_streak_games = []


    for game in games:

        #if the player is white
        if game["white"]["username"].lower() == username.lower():
             #if the player won the game
            if game["white"]["result"] == "win":
                # current_streak + 1
                current_streak += 1
                # add game to the current_streak_games
                current_streak_games.append(game)
            else: #if they lost the game
                #if current win streak is bigger than longest:
                
                    #make the longest streak equal the current streak
                    #make the streak_games list equal to current_streak games
                #reset current_streak to 0
                #reset current_streak_games to an empty list
