from GUI import Button
import actions

roll_button = Button((280,500), "GUI/images/buttons/button_roll_1.png", "GUI/images/buttons/button_roll_2.png", "GUI/images/buttons/button_roll_1.png")
def roll_button_function(game):
    roll1, roll2 = game.get_turns().roll()
    distance = roll1 + roll2
    if roll_button.over():
        actions.move(game.get_turns().current(), distance)

buy_button = Button((400,500), "GUI/images/buttons/button_buy_1.png", "GUI/images/buttons/button_buy_2.png", "GUI/images/buttons/button_buy_1.png")
def buy_button_function(game):
    pass

pay_rent_button = Button((200,500), "GUI/images/buttons/button_pay_rent_1.png", "GUI/images/buttons/button_pay_rent_2.png", "GUI/images/buttons/button_pay_rent_1.png")
def pay_rent_button_function(game):
    pass
