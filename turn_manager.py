import random

class TurnManager:
    """
    A class to manage the order of turns amongst game players.
    """

    def __init__(self, players):
        """
        Construct a new turn manager based on game players.

        Parameters:
            players (List<T>): An ordered list of players to store.
        """
        self._players = players
        # Start in correct direction
        self._direction = True
        self._location = 0
        self._max = len(players)
        self._status = True

    def current(self):
        return self._players[self._location]

    def next(self):
        self._status = True
        return self.skip(count=0)

    def get_player(self, position):
        return self._players[position]

    def status(self):
        return self._status

    def end_turn(self):
        self._status = False

    def skip(self, count=0):
        count += 1
        self._location += count
        self._location %= self._max
        return self._players[self._location]

    def roll(self):
        roll1, roll2 = random.randint(1,6), random.randint(1,6)
        # check double roll here
        return roll1, roll2

    def double_roll():
        return 0
