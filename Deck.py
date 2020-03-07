"""
Deck

Use get_decks() to initialize the decks
    deck_pot_luck, deck_opportunity_knocks = get_decks()

Use draw() to get the next card
    new_card = deck_pot_luck.draw()
"""


from Card import Card
from random import shuffle

class Deck:
    def __init__(self, deck_type):
        if deck_type == "Pot luck":
            self.init_pot_luck()
        if deck_type == "Opportunity knocks":
            self.init_opportunity_knocks()

    def draw(self):
        """
        Returns a Card object.
        If there are no cards remaining in the deck, returns a dummy Card object that does nothing, with ID=99.
        """
        if len(self.cards) == 0:
            print("ran out of cards!")
            return Card(99, "do nothing", "do nothing", self.deck_type)

        return self.cards.pop()


    def remaining_cards(self):
        """
        Returns the number of cards remaining in the deck.
        Simply returns the length of the list of Cards.
        """
        return len(self.cards)

    def shuffle(self):
        """
        Shuffles the deck.
        Uses python's list shuffle function to shuffle
        """
        shuffle(self.cards)

    def init_pot_luck(self):
        """
        Initializes a deck of Pot lucks.
        """
        PL1 = Card(1, "You inherit unichr(163)100", "Bank pays player 100", "Pot luck")
        PL2 = Card(2, "You have won 2nd prize in a beauty contest, collect unichr(163)20", "Bank pays player 20", "Pot luck")
        PL3 = Card(3,  "Go back to Crapper Street", "Player token moves backwards to Crapper Street", "Pot luck")
        PL4 = Card(4, "Student loan refund. Collect unichr(163)20", "Bank pays player 20", "Pot luck")
        PL5 = Card(5, "Bank error in your favour. Collect unichr(163)200", "Bank pays player 200", "Pot luck")
        PL6 = Card(6, "Pay bill for text books of unichr(163)100","Player pays 100 to the bank", "Pot luck")
        PL7 = Card(7, "Mega late night taxi bill pay unichr(163)50", "Player pays 50 to the bank", "Pot luck")
        PL8 = Card(8, "Advance to go", "Player moves forwards to GO", "Pot luck")
        PL9 = Card(9 , "From sale of Bitcoin you get unichr(163)50", "Bank pays player 50", "Pot luck")
        PL10 = Card(10, "Pay a unichr(163)10 fine or take opportunity knocks", "If fine paid, player puts 10 on free parking", "Pot luck")
        PL11 = Card(11, "Pay insurance fee of unichr(163)50", "Player puts 50 on free parking", "Pot luck")
        PL12 = Card(12, "Savings bond matures, collect unichar(163)100", "Bank pays 100 to the player", "Pot luck")
        PL13 = Card(13, "Go to jail. Do not pass GO, do not collect unichr(163)200", "As the card says", "Pot luck")
        PL14 = Card(14, "Received interest on shares of unichr(163)25", "Bank pays player 25", "Pot luck")
        PL15 = Card(15, "It's your birthday. Collect unichr(163)10 from each player", "Player receives 10 from each player", "Pot luck")
        PL16 = Card(16, "Get out of jail free", "Retained by the player until needed. No resale or trade value", "Pot luck")
        self.cards = [PL1,PL2,PL3,PL4,PL5,PL6,PL7,PL8,PL9,PL10,PL11,PL12,PL13,PL14,PL15,PL16]
        self.deck_type = "Pot luck"
        #self.shuffle()

    def init_opportunity_knocks(self):
        """
        Initializes a Deck of opportunity knocks
        """
        OK1 = Card(17, "Bank pays you divided of unichr(163)50", "Bank pays player 50", "Opportunity knocks")
        OK2 = Card(18, "You have won a lip sync battle. Collect unichr(163)100", "Bank pays player 100", "Opportunity knocks")
        OK3 = Card(19, "Advance to Turing Heights", "Player token moves forwards to Turing Heights", "Opportunity knocks")
        OK4 = Card(20, "Advance to Han Xin Gardens. If you pass GO, collect unichr(163)200", "Player moves token", "Opportunity knocks")
        OK5 = Card(21, "Fined unichr(163)15 for speeding", "Player puts 15 on free parking", "Opportunity knocks")
        OK6 = Card(22, "Pay university fees of unichr(163)150", "Player pays 150 to the bank", "Opportunity knocks")
        OK7 = Card(23, "Take a trip to Hove station. If you pass GO collect unichr(163)200", "Player moves token", "Opportunity knocks")
        OK8 = Card(24, "Loan matures, collect unichr(163)150", "Bank pays 150 to the player", "Opportunity knocks")
        OK9 = Card(25, "You are assessed for repairs, unichr(163)40/house, unichr(163)115/hotel", "Player pays money to the bank", "Opportunity knocks")
        OK10 = Card(26, "Advance to GO", "Player moves token", "Opportunity knocks")
        OK11 = Card(27, "You are assessed for repairs, unichr(163)25/house, unichr(163)100/hotel", "Player pays money to the bank", "Opportunity knocks")
        OK12 = Card(28, "Go back 3 spaces", "Player moves token", "Opportunity knocks")
        OK13 = Card(29, "Advance to Skywalker Drive. If you pass GO collect unichr(163)200", "Player moves token", "Opportunity knocks")
        OK14 = Card(30, "Go to jail. Do not pass GO, do not collect unichr(163)200", "As the card says", "Opportunity knocks")
        OK15 = Card(31, "Drunk in charge of a skateboard. Fine unichr(163)20", "Player puts 20 on free parking", "Opportunity knocks")
        OK16 = Card(32, "Get out of jail free", "Retained by the player until needed. No resale or trade value", "Opportunity knocks")
        self.cards = [OK1,OK2,OK3,OK4,OK5,OK6,OK7,OK8,OK9,OK10,OK11,OK12,OK13,OK14,OK15,OK16]
        self.deck_type = "Opportunity knocks"
        #self.shuffle()

def get_decks():
    deck_pot_luck = Deck("Pot luck")
    deck_opportunity_knocks = Deck("Opportunity knocks")
    return deck_pot_luck, deck_opportunity_knocks
