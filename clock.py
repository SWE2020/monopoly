import time
import pygame
import GUI
import datetime

class Clock:
        def __init__(self):
                self._start_time = time.time()

        def get_game_time(self):
                diff = time.time() - self._start_time
                return str(datetime.timedelta(seconds=diff))[0:7]

        def reset(self):
                self._start_time = time.time()

        def display_time(self, game):
                display = game.get_board().get_display()
                time_string = self.get_game_time()
                time_text = GUI.GameText((20,700), time_string, (40,40,40), 34)
                time_text.show(display)

        def abridged_check(self, game):
                if self.get_game_time() > game._time_limit:
                        game.terminate()
