from random import random, randint
from turn_manager import TurnManager
from player import Player
from board import Board
import GUI
import pygame
import clock

class Game:

    def __init__(self):

        self._players = []
        self._tokens = ["boot", "phone", "hat", "cat", "goblet", "spoon"]
        self.play_intro()


        self._turns = TurnManager(self._players)

        self._board = Board()

        self._board.setup_board()

        self._is_over = False
        self._winner = None

        self._last_roll = 0
        self._free_parking = 0
        self._clock = clock.Clock()

    def play_intro(self):
        pygame.mixer.music.load("soundtrack.ogg")
        pygame.mixer.music.play(-1)

        #num_players = GUI.game_intro()
        num_players = 4

        #player_names = GUI.select(num_players)
        player_names = ["Ege", "Kingsley", "Evan", "Kaleb"]

        for i in range(num_players):
            new_player = Player(player_names[i], self._tokens[i])
            self._players.append(new_player)


    def get_players(self):
        return self._players

    def get_board(self):
        return self._board

    def get_player(self, key):
        return self._players[key]

    def current_player(self):
        return self._turns.current()

    def get_next_player(self):
        return self._turns.next()

    def get_turns(self):
        return self._turns

    def is_over(self):
        return self._is_over

    def draw(self):
        self._board.draw_board(self)
