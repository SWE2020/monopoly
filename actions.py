# Import all other classes
from player import *
from Tile import *
from Deck import *
from Bank import *
from die import *
from board import *


def tile_land_handler(tile, player, game):
    if tile.can_be_bought():
        if tile.get_owner() == None:
            print("This property is not currently owned")
            property_purchase_handler(tile, player)
        else:
            property_owner = tile.get_owner()
            print("This property is owned by %s" % (property_owner.get_name()))
            # Pay rent
            transfer_money(player, property_owner, tile.get_rent())
            print("You pay %s in rent to %s" % (tile.get_rent(),
                                                property_owner.get_name()))
    else:
        action_tile_handler(tile, player, game)
# def card_action_handler(card, game):


def card_action_handler(card):
    print(card.Description)
    # TODO: Card subclasses or alter Card class to implement the actions
    # Card(int ID, string Description, char ActionInitial[P/M/J], list [Payer, Amount] Card_Type
    # or
    # class PaymentCard(Card), class MovementCard(Card), class JailFree(Card)
    # Case 1: Payment
    # Payer, Player, Amount

    # Case 2: Movement
    # Player, Location, Pass Go

    # Case 3: Jail Free
    # Player.JFCards += 1


def action_tile_handler(tile, player, game):
    tile_name = tile.get_name()
    if tile_name == "Go":
        # Do go functionality (Is it anything?) TODO
        x = 1

    elif tile_name == "Pot Luck":
        # Do the Pot Luck functionality
        card = game.get_pot_luck_deck().draw()
        card_action_handler(card)

    elif tile_name == "Opportunity Knocks":
        # Do the opportunity knocks
        card = game.get_opportunity_deck().draw()
        card_action_handler(card)
    elif tile_name == "Income Tax":
        # PAY 200 pounds
        player.decrease_balance(200)
        game.get_bank().deposit(200)

    elif tile_name == "Super Tax":
        # PAY 200 pounds
        player.decrease_balance(100)
        game.get_bank().deposit(100)

    elif tile_name == "Free Parking":
        # Collect all the fines
        fines = 1234
        player.increase_balance(fines)

    elif tile_name == "Go to Jail":
        print("Go to Jail")


def property_purchase_handler(tile, player):
    if player.has_passed_go():
        print("Current Options: | Buy | Auction |")
        choice = input("Pick an option: ")

        if choice == 'Auction':
            # Auction Handler
            print("Auction!!!")

        elif choice == 'Buy':
            # Add property to player's properties, give property the owner.
            player.buyProperty(tile)

def transfer_money(FROM, TO, amount):
    """ Transfers money from a player to another player"""
    FROM.bankBalance -= amount
    TO.bankBalance += amount
    # check if bankrupt?


def GO(player, bank):
    """Call this function when a player completes a full circle"""
    GO_money = 200
    bank.withdraw(GO_money)
    player.bankBalance += GO_money
    player.set_passed_go()


def move(player, distance):
    """
        Call this function to move a player around the board, given a distance.
        It checks for the following conditions:
                * A full lap around the board => invoke the GO function
                *
        """
    num_tiles = 39
    new_position = player.position + distance

    # check if the player completed a full lap around the board
    if new_position > num_tiles:
        new_position %= num_tiles
        # we will have to get bank from the Game.bank when Game.py is implemented
        bank1 = Bank(1000)
        # invoke GO
        GO(player, bank1)

    # update player's position to his new position
    player.position = new_position


def move_to(player, position):
    """
        Move player directly to a position within the board.
        """
    pass


def roll_dice(player):
    """
        Make a player roll the dice.
        Move the player.
        Check if the player rolled doubles.
        """
    # the dice should be re-initialized after we switch players
    # or simply set double_counter = 0

    dice = Die()
    dice_result = dice.roll()

    # move the player
    distance = sum(dice_result)
    move(player, distance)

    print("Dice roll value: " + str(dice_result))
    print("%s moves %s spaces" % (player.getPlayerName(), dice_result))

    # check if doubles for the first time => it's player's turn again
    if dice.double_counter == 1:
        # game.setplayer
        pass
    # check if doubles for the second time => go to jail
    if dice.double_counter == 2:
        go_to_jail(player)


def go_to_jail(player):
    """
        Send a player to jail.
        """
    # update player's jail field
    player.setInJail(True)
    # teleport the player to the jail's position
    jail_position = 15
    player.setPosition(jail_position)

# transfer property?

# card actions! (another file?)
