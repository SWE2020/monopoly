class Player:

    def __init__(self, name, token):
        self.playerName = name
        self.tokenName = token
        self.bankBalance = 1000

        self.position = 0

        self.propertiesOwned = []
        self.propertiesMortgaged = []

        self.hasWon = False
        self.inJail = False
        self._passed_go_once = True
        self._double_counter = 0
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

    #add a property to the array of properties owned
    def addPropertyOwned(prop):
        self.propertiesOwned.append(prop)

    #should be called in GameManager after initial go-around?
    def passedGoOnce():
        self.passedGoOnce = True


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
