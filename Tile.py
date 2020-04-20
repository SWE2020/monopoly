import pygame
import GUI

class Tile:
    """ An abstract representation of a Monopoly game tile

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            can_be_bought: A boolean that indicates whether this tile can be bought
            """

    def __init__(self, position, name, can_be_bought, image):
        """ Creates an instance of the Tile object

            Should not be instantiated directly. """

        self._name = name
        self._position = position
        self._can_be_bought = can_be_bought
        self._image = GUI.utils.rescale(pygame.image.load(image), 0.20)

    def get_name(self):
        """ Returns:
            The name of the Tile object as a string """
        return self._name

    def get_position(self):
        """ Returns:
            Intended position of the Tile within the Board as an integer. """
        return self._position

    def can_be_bought(self):
        """ Returns:
            True, if the Tile can be bought in-game, otherwise returns false. """
        return self._can_be_bought

    def get_image(self):
        """ Returns:
            The image for tile"""
        return self._image


class ActionTile(Tile):
    """ A Monopoly game tile that triggers special interactions within the game.

        An ActionTile instance cannot be purchased by an agent within the game. Instead,
        instance specific actions will occur to players when this Tile is landed on.

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            TODO: add this to make it more speciifc
            action: An Action instance that provides output ....
            can_be_bought: A boolean that indicates whether this tile can be bought
    """

    def __init__(self, position, name, action, can_be_bought=False, image=None):

        """ Creates an instance of the ActionTile class

            Args:
                position: An unique integer indicating its position within the Monopoly board
                name: A unique string of the tile's name
                can_be_bought: A boolean that indicates whether this tile can be bought
                TODO: add this to make it more speciifc
                action: An Action instance that provides output ....

        """

        super().__init__(position, name, can_be_bought, image)

        self._action = action

    def get_action(self):
        """ Returns:
            The action for instance """
        pass


class PropertyTile(Tile):
    """ A tile in Monopoly that represents a single property

        A PropertyTile instance can be purchased by an agent within the game. If the property is developed within
        Monopoly, the rent of an instance of PropertyTile will increase depending on the amount of houses that a
        property has.

        Attributes:
            position: An unique integer indicating its position within the Monopoly board
            name: A unique string of the tile's name
            group: A string indicating the group of tiles this instance belongs to
            can_be_bought=True: A boolean that indicates whether this tile can be bought
            cost: An integer that indicates the amount of money that is required to purchase this property
            rent: An integer indicating the default, total amount of rent assigned to this property
            house_rent_1: An integer of the total amount of rent, if the property has 1 houses
            house_rent_2: An integer of the total amount of rent, if the property has 2 houses
            house_rent_3: An integer of the total amount of rent, if the property has 3 houses
            house_rent_4: An integer of the total amount of rent, if the property has 4 houses
            hotel_rent: An integer of the total amount of rent, if the property has a hotel
        """
    def __init__(self, position, name, group, cost, rent, house_rent_1, house_rent_2,
                 house_rent_3, house_rent_4, hotel_rent, can_be_bought=True, image=None):

        """ Creates an instance of PropertyTile with the arguments assigned to the attributes of PropertyTile.

         Args:
             position: An integer indicating its position within the Monopoly board
            name: A string of the tile's name within PropertyTycoon
            group: A string indicating the group of tiles this instance belongs to
            can_be_bought=True: A boolean that indicates whether this tile can be bought
            cost: An integer that indicates the amount of money that is required to purchase this property
            rent: An integer indicating the default, total amount of rent assigned to this property
            house_rent_1: An integer of the total amount of rent, if the property has 1 houses
            house_rent_2: An integer of the total amount of rent, if the property has 2 houses
            house_rent_3: An integer of the total amount of rent, if the property has 3 houses
            house_rent_4: An integer of the total amount of rent, if the property has 4 houses
            hotel_rent: An integer of the total amount of rent, if the property has a hotel
            """

        super().__init__(position, name, can_be_bought, image)

        self._group = group
        self._cost = cost
        self._rent = rent
        self._house_rent = [house_rent_1, house_rent_2, house_rent_3, house_rent_4]
        self._hotel_rent = hotel_rent
        self._num_houses = 0
        self._num_hotel = 0

    def get_house_count(self):
        """ Returns:
            An integer of the current amount of houses assigned to this property """
        return self._num_houses

    def get_hotel_count(self):
        """ Returns:
            An integer of the current amount of hotels assigned to this property"""
        return self._num_hotel

    def get_cost(self):
        """ Returns:
            The integer amount that this property costs"""
        return self._cost

    def add_house(self):
        """ Adds a house to the property. If there are 4 houses on this property, a house will not be added.

            Returns:
                A boolean indicating whether a house has been successfully added to the property.
                True, if there are less than 4 houses. False, otherwise.  """
        if self._num_houses != 4:
            self._num_houses += 1
            # print("You have purchased a house for " + self.get_name())
            return True
        else:
            # print("There are already 4 houses. You cannot add another house. Buy a hotel instead.")
            return False

    def add_hotel(self):
        """ Adds a hotel to the property. If there are less than 4 houses on this property, a hotel will not be added.
            If a hotel is already on this property, a hotel will not be added.

            Returns:
                A boolean indicating whether a hotel has been successfully added.
                True, if there 4 houses. False, otherwise.
        """
        if self._num_houses < 4:
            # print("You need 4 houses to purchase a hotel. Buy a house instead")
            return False

        elif self._num_hotel:
            # print("you already have a hotel, you cannot buy another")
            return False

        else:
            self._num_hotel = 1
            self._num_houses = 0
            # print("You have purchased a hotel for " + self.get_name())
            return False

    def get_rent(self):
        """ Returns:
            The integer amount of rent that this property will incur, depending on the amount of houses or hotels
            purchased for this property. """
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
