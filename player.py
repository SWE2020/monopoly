##import Property

class Player:
    #initialize all
    def __init__(self ):
        #input from player
        self.playerName = ""
        #name of token piece
        self.tokenName = ""
        self.bankBalance = 0
        #position on board in regards to board array
        self.position = [0,0]
        #holds an array of Property objects
        self.propertiesOwned = []
        #holds an array of Property objects
        self.propertiesMortgaged = []
        self.hasWon = False
        self.inJail = False
        jailTimeCount = 0

    def getPlayerName(self):
        return self.playerName

    def setPlayerName(self, pname):
        self.playerName = pname

    def getTokenName(self):
        return self.tokenName

    def setTokenName(self, tname):
        self.tokenName = tname

    def getBankBalance(self):
        return self.bankBalance

    def setBankBalance(self, balance):
        self.bankBalance = balance

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getJailTimeCount(self):
        return self.jailTimeCount

    def setJailTimeCount(self, jailTime):
        self.jailTimeCount = jailTime

    def getHasWon(self):
        return self.hasWon

    def setHasWon(self):
        self.hasWon = True

    def getInJail(self):
        return self.inJail

    def setInJail(self):
        self.inJail = True

    def getPropertiesOwned(self):
        return self.propertiesOwned

    def setPropertiesOwned(self):
        return True
    def getPropertiesMortgaged(self):
        return self.propertiesMortgaged

    def setPropertiesMortgaged(self):
        return True
        
