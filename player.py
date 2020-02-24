import Property

class Player:
    #initialize all
    def __init__(self):
        #input from player
        self.playerName = ""
        #name of token piece
        self.tokenName = ""
        self.ankBalance = 0
        #position on board in regards to board array
        self.position = [0,0]
        #holds an array of Property objects
        self.propertiesOwned = []
        #holds an array of Property objects
        self.propertiesMortgaged = []
        self.hasWon = false
        self.inJail = false
        jailTimeCount = 0
        
