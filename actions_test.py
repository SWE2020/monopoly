from actions import *

"""
Test: transfer_money
"""
print("Testing: transfer_money")
player1 = Player("Ege", "token1")
player1.bankBalance = 1000
player2 = Player("Kaleb", "token2")
player2.bankBalance = 1000

transfer_money(player1, player2, 100)

print(player1.bankBalance == 900)
print(player2.bankBalance == 1100)


"""
Test: GO
"""
print("Testing: GO")
player1 = Player("Ege", "token1")
player1.bankBalance = 1000
bank1 = Bank(1000)

GO(player1, bank1)

print(bank1.balance == 800)
print(player1.bankBalance == 1200)


"""
Test: move
"""
print("Testing: move")

player1 = Player("Ege", "token1")
player1.bankBalance = 0

move(player1, 50)

print(player1.bankBalance == 200)
print(bank1.balance == 800)
