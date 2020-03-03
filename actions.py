# Import all other classes
from Player import *
from Tile import *
from Deck import *
from Bank import *

# Actions:

def transfer_money(FROM, TO, amount):
        """ Transfers money from a player to another player"""
        FROM.bankBalance -= amount
        TO.bankBalance += amount
        # check if bankrupt?

"""
Test: transfer_money

# create players for testing
player1 = Player()
player1.bankBalance = 1000
player2 = Player()
player2.bankBalance = 1000

transfer_money(player1, player2, 100)

print(player1.bankBalance == 900)
print(player2.bankBalance == 1100)
"""

def GO(player, bank):
        GO_money = 200
        bank.withdraw(GO_money)
        player.bankBalance += GO_money

"""
Test: GO
player1 = Player()
player1.bankBalance = 1000
bank1 = Bank(1000)

GO(player1, bank1)

print(bank1.balance == 800)
print(player1.bankBalance == 1200)
"""

def move(player, distance):
        num_tiles = 40
        new_position = player.position + distance
e
        if new_position > num_tiles:
                new_position %= num_tiles
                GO(player, bank1)

"""
Test: move
player1 = Player()
bank1 = Bank(200)
player1.bankBalance = 100
move(player1, 50)
print(player1.bankBalance == 300)
print(bank1.balance == 0)
"""
