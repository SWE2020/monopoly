from GUI import Button
import actions

button_roll = Button((350,520), "GUI/images/buttons/button_roll_1.png", "GUI/images/buttons/button_roll_2.png", "GUI/images/buttons/button_roll_1.png")
def button_roll_function(game):
    actions.roll_dice(game)


button_buy = Button((250,520), "GUI/images/buttons/button_buy_1.png", "GUI/images/buttons/button_buy_2.png", "GUI/images/buttons/button_buy_1.png")
def button_buy_function(game):
    current_player = game.get_turns().current()
    current_position = current_player.getPosition()
    current_tile = game.get_board().get_tile_at(current_position)
    actions.buy_property(current_player, current_tile)
    

button_pay_rent = Button((250,520), "GUI/images/buttons/button_pay_rent_1.png", "GUI/images/buttons/button_pay_rent_2.png", "GUI/images/buttons/button_pay_rent_1.png")
def button_pay_rent_function(game):
    current_player = game.get_turns().current()
    current_position = current_player.getPosition()
    current_tile = game.get_board().get_tile_at(current_position)
    owner = current_tile._owner
    amount = current_tile.get_cost()
    actions.transfer_money(current_player, owner, amount)

button_end_turn = Button((450,520), "GUI/images/buttons/button_end_turn_1.png", "GUI/images/buttons/button_end_turn_2.png", "GUI/images/buttons/button_end_turn_1.png")
def button_end_turn_function(game):
    return "End Turn"
