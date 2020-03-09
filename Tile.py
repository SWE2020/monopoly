class Tile:
    """ Base case class for board tile object """


    def __init__(self, position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent):
        """ An abstract representation of a Monopoly game tile 
         
            Should not be instantiated directly. """

        self._name = name
        self._group = group
        self._position = position
        self._action = action
        self._can_be_bought = can_be_bought
        self._cost = cost
        self._rent = rent
        self._house_rent = [house_rent_1, house_rent_2, house_rent_3, house_rent_4]
        self._hotel_rent = hotel_rent

    def get_name(self):
        """ Returns the name of the Tile object as a string """
        return self._name

    def get_position(self):
        """ Returns intended position of the Tile within the Board as an integer. """
        return self._position

    def can_be_bought(self):
        """ Returns true if the Tile can be bought in-game, otherwise returns false. """
        return self._can_be_bought

    ## Only for properties
    def get_cost(self):
        """ Returns the cost of buying this Tile, iff the Tile can be purchased in-game. """
        pass

    def get_house_rent(self, house_count):
        pass

    def get_hotel_rent(self):
        pass


    ## Only for action cards
    def get_action(self):
        """ Returns the action that must be undertaken in-game as a string. """
        pass


class ActionTile(Tile):
    """ A tile in Monopoly that represents an action """

    def __init__(self, position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent):

        super().__init__(position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent)

        self._action = action

    def get_action(self):
<<<<<<< Updated upstream
        pass
=======
        return self._action

    def perform_action(self):
        """ Returns:
                The action for instance """
        print(self._name)
        print(self._action)
>>>>>>> Stashed changes


class PropertyTile(Tile):
    """ A tile in Monopoly that represents a property"""
    def __init__(self, position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent):

        super().__init__(position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent)

        self._num_houses = 0
        self._num_hotel = 0
        self._owner = None

    def get_house_count(self):
        return self._num_houses

    def get_hotel_count(self):
        return self._num_hotel

    def get_cost(self):
        return self._cost

    def get_owner(self):
        return self._owner

    def add_house(self):
        if self._num_houses != 4:
            self._num_houses += 1
            # print("You have purchased a house for " + self.get_name())
            return 1
        else:
            # print("There are already 4 houses. You cannot add another house. Buy a hotel instead.")
            return 0

    def add_hotel(self):
        if self._num_houses < 4:
            # print("You need 4 houses to purchase a hotel. Buy a house instead")
            return 0

        elif self._num_hotel:
            # print("you already have a hotel, you cannot buy another")
            return 0

        else:
            self._num_hotel = 1
            self._num_houses = 0
            # print("You have purchased a hotel for " + self.get_name())
            return 1



    def get_rent(self):
        if self.get_hotel_count():
            # print("There is one hotel. The rent is: " + str(self._hotel_rent))
            return self._hotel_rent
        elif self.get_house_count():
            # print("There are " + str(self.get_house_count()) +
            #       " houses. Rent is: " + str(self._house_rent[self.get_house_count() - 1]))
            return self._house_rent[self.get_house_count() - 1]
        else:
            # print("Nothing, base rent then: " + str(self._rent))
            return self._rent


class ActionTile(Tile):
    def __init__(self, position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent):

        super().__init__(position, name, group, action, can_be_bought, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent)

    def get_action(self):
        return self._action

