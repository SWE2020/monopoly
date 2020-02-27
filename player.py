#import Property
#import Die

class Player:
    #initialize all
    def __init__(self):
        #input from player
        self.playerName = ""
        #name of token piece
        self.tokenName = ""
        #true means a real player, false means AI
        #might need a better name
        self.realPlayer = true
        #amount each player gets at the beginning of the game
        self.bankBalance = 1500
        #number of times a player has rolled the dice in a single turn; max is 3
        self.diceRolls = 0
        #position on board in regards to board array; position 0 is the 'GO' tile and where every player starts
        self.position = 0
        #holds an array of Property objects
        self.propertiesOwned = []
        #holds an array of Property objects
        self.propertiesMortgaged = []
        self.hasWon = false
        self.inJail = false
        #initially set to false because no player starts out with this card
        self.hasGetOOJailFreeCard = false
        #rounds that a player has been in jail; max is 3
        self.jailTimeCount = 0



    def getPlayerName():
        return self.playerName

    #this should get called in the GameManager
    def setPlayerName(pname):
        self.playerName = pname

    def getTokenName():
        return self.tokenName

    #this should get called in the GameManager
    def setTokenName(tname):
        self.tokenName = tname

    #returns amount in a player's bank account
    def getBankBalance():
        return self.bankBalance

    #adds the amount passed to a players account
    #should this handle subtractions or should that be a separate function?
    def addToBankBalance(addAmount):
        self.bankBalance += addAmount

    def subtractFromBankBalance(subAmount):
        self.bankBalance -= subAmount

    def getPosition():
        return self.position

    #sets a players position on the board; should be passed the dice roll
    #not sure if this should be a +position or just setting it to new position
    def setPosition(position):
        self.position += position

    #returns the number of rounds a player has been in jail; should not surpass 3
    def getJailTimeCount():
        return self.jailTimeCount

    #increments jail time by 1
    def incrementJailTimeCount():
        self.jailTimeCount += 1

    #returns the win status of a player
    def getHasWon():
        return self.hasWon

    #sets a players win status; true means they have won, false means they haven't won
    def setHasWon(hasWon):
        self.hasWon = hasWon

    #returns whether a player is in jail or not
    def getInJail():
        return self.inJail

    #sets a players jail status; true means in jail, false means not in jail
    def setInJail(inJail):
        self.inJail = inJail

    #pass true if player received a 'Get Out of Jail Free' card, pass false if the player used it
    def setGetOOJailFreeCard(hasCard):
        self.hasGetOOJailFreeCard = hasCard

    #return the array of properties owned
    def getPropertiesOwned():
        return self.propertiesOwned

    #checks to see if a player can purchase a property; will return false if the player doesn't have
    #enough funds; else will return true, subtract property cost from player's bank account, and add
    #property to list of player's properties
    #dependent on implementation of property class
    def buyProperty(property):
        bankBalance = self.getBankBalance
        propertyPrice = property.getPrice()
        if propertyPrice > bankBalance:
            return false
        else:
            self.subtractFromBankBalance(propertyPrice)
            self.addPropertyOwned(property.getDetails)
            return true

    #add a property to the array of properties owned
    def addPropertyOwned(propertiesOwned):
        self.propertiesOwned.append(propertiesOwned)

    def passedGo():
        self.bankBalance += 2000

    #def rollDice():
