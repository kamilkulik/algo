from src.tournament_winner.tournament_winner import tournament_winner   

test_cases = [
    {
        "competitions": [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ],
        "results": [0, 0, 1],
        "winner": "Python",
    },
    {
        "competitions": [
            ["HTML", "Java"],
            ["Java", "Python"],
            ["Python", "HTML"],
            ["C#", "Python"],
            ["Java", "C#"],
            ["C#", "HTML"],
            ["SQL", "C#"],
            ["HTML", "SQL"],
            ["SQL", "Python"],
            ["SQL", "Java"]
        ],
        "results": [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        "winner": "C#",
    },
    {
        "competitions": [
            ["Bulls", "Eagles"]
        ],
        "results": [1],
        "winner": "Bulls",
    },
    {
        "competitions": [
            ["AlgoMasters", "FrontPage Freebirds"],
            ["Runtime Terror", "Static Startup"],
            ["WeC#", "Hypertext Assassins"],
            ["AlgoMasters", "WeC#"],
            ["Static Startup", "Hypertext Assassins"],
            ["Runtime Terror", "FrontPage Freebirds"],
            ["AlgoMasters", "Runtime Terror"],
            ["Hypertext Assassins", "FrontPage Freebirds"],
            ["Static Startup", "WeC#"],
            ["AlgoMasters", "Static Startup"],
            ["FrontPage Freebirds", "WeC#"],
            ["Hypertext Assassins", "Runtime Terror"],
            ["AlgoMasters", "Hypertext Assassins"],
            ["WeC#", "Runtime Terror"],
            ["FrontPage Freebirds", "Static Startup"]
        ],
        "results": [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        "winner": "AlgoMasters",
    }
]

def test_tournament_winner_1():
    for test_case in test_cases:
        competitions = test_case["competitions"]
        results = test_case["results"]
        winner = test_case["winner"]
        assert tournament_winner(competitions, results) == winner