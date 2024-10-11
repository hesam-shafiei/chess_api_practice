# main.py

import helper
import pprint

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
                if current_streak > longest_streak:
                    #make the longest streak equal the current streak
                    longest_streak = current_streak
                    streak_games = current_streak_games[:]
                    #make the streak_games list equal to current_streak games
                #reset current_streak to 0
                current_streak = 0
                #reset current_streak_games to an empty list
                current_streak_games = []

        if game["black"]["username"].lower() == username.lower():
            if game["black"]["result"] == "win":
                current_streak += 1
                current_streak_games.append(game)
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    streak_games = current_streak_games[:]
                current_streak = 0
                current_streak_games = []

    if current_streak > longest_streak:
        longest_streak = current_streak
        streak_games = current_streak_games[:]

    print(f"Longest win streak: {longest_streak} games")
    print("Games in the win streak: ")
    counter = 1
    for game in streak_games:
        url = game["url"]
        print(f"{counter}. {url}")
        counter += 1



def longest_loss_streak(username, year, month):
    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    longest_streak = 0
    current_streak = 0
    streak_games = []
    current_streak_games = []

    for game in games:
        # if the player is white
        if game["white"]["username"].lower() == username.lower():
            # if the player lost the game
            if game["black"]["result"] == "win":
                # current_streak + 1
                current_streak += 1
                # add game to the current_streak_games
                current_streak_games.append(game)
            else:  # if they did not lose
                # if current loss streak is bigger than the longest:
                if current_streak > longest_streak:
                    # make the longest streak equal the current streak
                    longest_streak = current_streak
                    streak_games = current_streak_games[:]
                # reset current_streak to 0
                current_streak = 0
                # reset current_streak_games to an empty list
                current_streak_games = []

        # if the player is black
        elif game["black"]["username"].lower() == username.lower():
            # if the player lost the game
            if game["white"]["result"] == "win":
                current_streak += 1
                current_streak_games.append(game)
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                    streak_games = current_streak_games[:]
                current_streak = 0
                current_streak_games = []

    # After the loop, check if the last streak is the longest
    if current_streak > longest_streak:
        longest_streak = current_streak
        streak_games = current_streak_games[:]

    print(f"Longest loss streak: {longest_streak} games")
    print("Games in the loss streak: ")
    counter = 1
    for game in streak_games:
        url = game["url"]
        print(f"{counter}. {url}")
        counter += 1


#longest_win_streak("chess_hesam", 2024, 6)
#top_games_of_month("mrvicious1", 2024, 8)
#worst_games_of_month("generalzod", 2024, 9)
# longest_loss_streak("chess_hesam", 2024, 8)

# https://api.chess.com/pub/player/chess_hesam/games/2024/07


def most_common_opening(username, year, month):

    data = helper.fetch_monthly_data(username, year, month)
    games = data.get("games")

    openings_count = {}

    # openings_count = {
    #     "pirc_defense":{
    #         "games_played": 2,
    #         "wins": 1,
    #         "losses": 0,
    #         "draws": 1
    #     },
    #     "karo-kann-defense":{
    #         "games_played": 2,
    #         "wins": 1,
    #         "losses": 0,
    #         "draws": 1
    #     }
    
    # }

    for game in games:
        if "eco" in game:
            #extract the opening name from a url like this: 
            #https://www.chess.com/openings/Caro-Kann-Defense-2.d4-d5-3.Nc3
            #it extracts Caro-Kann-Defense-2.d4-d5-3.Nc3
            opening_name = game['eco'].split('/')[-1]

            #checking if this opening already exists in our opening count object
            if opening_name not in openings_count:
                openings_count[opening_name] = {
                    "games_played": 0,
                    "wins": 0,
                    "losses": 0,
                    "draws": 0
                }
            openings_count[opening_name]["games_played"] += 1
            
            #if the username is playing as white
            if game["white"]["username"].lower() == username.lower():
                #if white has the same result as black (a tie)
                if game["white"]["result"] == game["black"]["result"]:
                    openings_count[opening_name]["draws"] += 1
                #if white won
                elif game["white"]["result"] == "win":
                    openings_count[opening_name]["wins"] += 1
                #if white lost
                else:
                    openings_count[opening_name]["losses"] += 1


    sorted_openings = dict(sorted(openings_count.items(), key=lambda x: x[1]["games_played"], reverse=True))
    
    
    print(sorted_openings)

most_common_opening("chess_hesam", 2024, 9)




# https://api.chess.com/pub/player/chess_hesam/games/2024/07