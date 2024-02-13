"""Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)"""
no_of_games_played_in_tournament = eval(
    input("number of games played in a tournament= ")
)
games_won = eval(input("Enter no of games you won ="))
games_loss = eval(input("Enter no of games you loss ="))
tie = no_of_games_played_in_tournament - (games_won + games_loss)
print(f"{tie=}")
total_points = games_won * 4 + tie * 2
print(f"{total_points =}")
