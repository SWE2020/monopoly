from GUI import Button
import actions

roll_button = Button((250,500), "GUI/images/buttons/button_roll_1.png", "GUI/images/buttons/button_roll_2.png", "GUI/images/buttons/button_roll_1.png")

def roll_button_function(game):
    roll1, roll2 = game.get_turns().roll()
    distance = roll1 + roll2
    if roll_button.over():
        actions.move(game.get_turns().current(), distance)
