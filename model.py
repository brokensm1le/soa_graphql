from collections import namedtuple

scoreboard = namedtuple("scoreboard", ["who_win"])
Game = namedtuple("Game", ["id", "scoreboard", "status", "comments"])

data = {
    1: Game(1, scoreboard("mafia"), "finished", ""),
    2: Game(2, scoreboard("civilians"), "finished", ""),
    3: Game(3, scoreboard("None"), "going on", ""),
    4: Game(4, scoreboard("None"), "going on", ""),
}