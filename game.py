from random import random, randint
from turn_manager import TurnManager
from player import Player
from board import Board
import GUI
import pygame
import clock
import display_token
import display_tile

class Game:

    def __init__(self):

        self._players = []
        self._tokens = ["boot", "phone", "hat", "cat", "goblet", "spoon"]

        self._MUSIC = True
        self._TESTING = False

        self.play_intro()

        self._turns = TurnManager(self._players)
        self._board = Board()
        self._board.setup_board()

        self._is_over = False
        self._winner = None

        self._last_roll = 0
        self._free_parking = 0
        self._clock = clock.Clock()
        self._time_limit = "0:00:30"

    def play_intro(self):

        if self._MUSIC:
            pygame.mixer.music.load("soundtrack.ogg")
            pygame.mixer.music.play(-1)

        if self._TESTING:
            num_players = 3
            player_names = ["Ege", "Kingsley", "Evan"]
            self._mode = "Full"
        else:
            num_players = GUI.game_intro()
            player_names = GUI.select(num_players)
            self._mode = GUI.mode_select()

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

    def remove_current_player(self):
        self._turns.remove_current_player()

    def get_display(self):
        return self.get_board().get_display()

    def draw(self):
        """
        Do this every frame.
        """
        self._board.draw_board(self)
        self.check_termination()

    def terminate(self):
        # pick winner
        winner_name = self.pick_winner().getPlayerName()

        while True:
        # message
            display = self.get_display()

            # background
            display.fill((20,20,20))

            # crown
            crown_image = pygame.image.load("GUI/images/crown.png")
            display.blit(crown_image, (400, 100))

            # winner text
            out_string = winner_name
            x,y = pygame.mouse.get_pos()
            out_text = GUI.GameText((500,500), out_string, (255,255,255), 85)
            out_text.textRect.center = (715,580)

            out_text.show(display)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(x,y)
                if event.type == pygame.QUIT:
                    quit()
                    pygame.quit()

            pygame.display.update()



    def pick_winner(self):
        max_asset = 0
        winner = self._players[0]
        for p in self._players:
            assets = p.calculate_assets()
            if assets > max_asset:
                winner = p
                max_asset = assets
        return winner

    def check_termination(self):
        if len(self._players) == 1:
            self.terminate()
        if self._mode == "Abridged":
            self._clock.abridged_check(self)
