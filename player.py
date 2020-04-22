class Player:
    #initialize all
    def __init__(self, name, token):
        #input from player
        self.playerName = name
        #name of token piece
        self.tokenName = token
        self.bankBalance = 1000
        #position on board in regards to board array

        self.position = 0
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

    #sets a players jail status; true means in jail, false means not in jail
    def setInJail(inJail):
        self.inJail = inJail

    #pass true if player received a 'Get Out of Jail Free' card, pass false if the player used it
    def setGetOOJailFreeCard(hasCard):
        self.hasGetOOJailFreeCard = hasCard

    #return the array of properties owned
    def getPropertiesOwned(self):
        # Changed this so that we could get the names ofo the properties owned
        #return self.propertiesOwned
        empty = []
        for i in self.propertiesOwned:
            empty.append(i.get_name())
        return empty

    def setPropertiesOwned(self):
        return True

    def getPropertiesMortgaged(self):
        return self.propertiesMortgaged

    def setPropertiesMortgaged(self):
        return True

    #checks to see if a player can purchase a property; will return false if the player doesn't have
    #enough funds; else will return true, subtract property cost from player's bank account, and add
    #property to list of player's properties
    #dependent on implementation of property class
    def buyProperty(property):
        if(passedGoOnce):
            bankBalance = self.getBankBalance
            propertyPrice = property.getPrice()
            if propertyPrice > bankBalance:
                return false
            else:
                self.subtractFromBankBalance(propertyPrice)
                self.addPropertyOwned(property.getDetails)
                return true
        else:
            return false

    #add a property to the array of properties owned
    def addPropertyOwned(propertiesOwned):
        self.propertiesOwned.append(propertiesOwned)

    #should be called in GameManager after initial go-around?
    def passedGoOnce():
        self.passedGoOnce = true

    def passedGo():
        self.bankBalance += 2000

    def rollDice():
        die = Die()
        currRoll = die.roll()
        self.diceRolls = self.diceRolls + 1
        totalRoll = currRoll[0] + currRoll[1]
        if currRoll[0] == currRoll[1]:
            self.setPosition(totalRoll)
            currRoll = die.roll()
            self.diceRolls = self.diceRolls + 1
            totalRoll = currRoll[0] + currRoll[1]
            if currRoll[0] == currRoll[1]:
                self.setPosition(totalRoll)
                currRoll = die.roll()
                self.diceRolls = self.diceRolls + 1
                totalRoll = currRoll[0] + currRoll[1]
            else:
                self.setPosition(totalRoll)
                if currRoll[0] == currRoll[1]:
                    self.goToJail()
                else:
                    self.setPosition(totalRoll)
        else:
            self.setPosition(totalRoll)

    #returns true if successful, false if they dont have enough money
    #this is dependent on implementation of the Property class and how that will deal
    #with houses and hotels
    def buyHouseOrHotel(property):
        bankBalance = self.getBankBalance
        price = property.getPrice
        if price > bankBalance:
            return false
        else:
            self.subtractFromBankBalance(price)
            property.addHotel()
            return true
