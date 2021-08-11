import pytest
from src.tournament_winner.tournament_winner import tournament_winner, tournament_winner_alt

test_cases = [
    (
        [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ], [0, 0, 1], "Python",
    ),
    (
        [
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
        ], [0, 1, 1, 1, 0, 1, 0, 1, 1, 0], "C#",
    ),
    (
        [
            ["Bulls", "Eagles"]
        ], [1], "Bulls",
    ),
    (
        [
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
        ], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], "AlgoMasters",
    )
]

@pytest.mark.parametrize('competitions, results, winner', test_cases)
def test_tournament_winner(competitions, results, winner):
    assert tournament_winner(competitions, results) == winner

@pytest.mark.parametrize('competitions, results, winner', test_cases)
def test_tournament_winner(competitions, results, winner):
    assert tournament_winner_alt(competitions, results) == winner