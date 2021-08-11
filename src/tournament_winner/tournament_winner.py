# competitions: [home_team, away_team]
# results: 1 - home team won, 0 - away team won
# results[i] has results for the match competitions[i]
# winner gets 3 points
# loser gets 0 points

# COMPLEXITY
# TIME O(n)
# SPACE O(c) where c is the number of competitions

def tournament_winner(competitions, results):
    scores = {}
    highest_score = 0
    tournament_winner = ""
    for idx, match in enumerate(competitions):
        home_team = match[0]
        away_team = match[1]

        current_winner = home_team if results[idx] == 1 else away_team
    
        if current_winner not in scores:
            scores[current_winner] = 0
        scores[current_winner] += 3

        if scores[current_winner] > highest_score:
            highest_score = scores[current_winner]
            tournament_winner = current_winner

    return tournament_winner


# 1. initiate variable that will denote win for the home team
HOME_TEAM_WON = 1

def tournament_winner_alt(competitions, results):
    # 2. Initiate a dict which will serve as a log of:
    # the highest score achieved so far
    # names of the teams with their respective scores
    scores = { "current_best_team": 0}

    # 3. initiate a variable to keep track of the best team at each point of the competitions array
    current_best_team = ""

    # 4. iterate over competitions array with for + enumerate - we'll need both idx and values
    for idx, match in enumerate(competitions):
        home_team, away_team = match

        # 5. determine winner of the current match (current iteration)
        current_winner = home_team if results[idx] == HOME_TEAM_WON else away_team
        # 6. update the scores using a helper function
        update_scores(current_winner, 3, scores)

        # 7. check if the current winner has more points that the current_best_team in the log
        # if yes update current_best_team variable and current_best_team score
        if scores[current_winner] > scores["current_best_team"]:
            current_best_team = current_winner
            scores["current_best_team"] = scores[current_winner]

    return current_best_team

def update_scores(current_winner, points, scores):
    if current_winner not in scores:
        scores[current_winner] = 0
    scores[current_winner] += points