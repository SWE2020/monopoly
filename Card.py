class Card:
    def __init__(self, ID, Description, Action, Card_Type):
        self.ID = ID
        self.Description = Description
        self.Card_Type = Card_Type
        self.Action = Action

    def get_ID(self):
        return self.ID

    def get_Description(self):
        return self.Description

    def get_Card_Type(self):
        return self.Card_Type
