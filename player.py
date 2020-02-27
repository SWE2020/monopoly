import Property

class Player:
    #initialize all
    def __init__(self):
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
        self.hasWon = false
        self.inJail = false
        jailTimeCount = 0

    def getPlayerName():
        return self.playerName

    def setPlayerName(pname):
        self.playerName = pname

    def getTokenName():
        return self.tokenName

    def setTokenName(tname):
        self.tokenName = tname

    def getBankBalance():
        return self.bankBalance

    def setBankBalance(balance):
        self.bankBalance = balance

    def getPosition():
        return self.position

    def setPosition(position):
        self.position = position

    def getJailTimeCount():
        return self.jailTimeCount

    def setJailTimeCount(jailTime):
        self.jailTimeCount = jailTime

    def getHasWon():
        return self.hasWon

    def setHasWon(hasWon):
        self.hasWon = hasWon

    def getInJail():
        return self.inJail

    def setInJail(inJail):
        self.inJail = inJail

    def getPropertiesOwned():
        return self.propertiesOwned

    def setPropertiesOwned(propertiesOwned):

    def getPropertiesMortgaged():
        return self.propertiesMortgaged

    def setPropertiesMortgaged(propertiesMortgaged):
        
