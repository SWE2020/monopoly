class Card:
    def __init__(self, card_id, card_type, description, action_data):
        self._card_id = card_id
        self._card_type = card_type
        self._description = description
        self._action_data = action_data
        # self.Action = Action

    def get_id(self):
        return self._card_id

    def get_type(self):
        return self._card_type

    def get_description(self):
        return self._description

    def action_data(self):
        return self._action_data

    # def get_card_type(self):
    #     return self.Card_Type


class PaymentCard(Card):

    def __init__(self, card_id, card_type, description, action_data):

        super().__init__(card_id, card_type, description, action_data)
        self._pay_from = None
        self._pay_to = None
        self._amount = None

    def upack_action_data(self):
        pass

    def perform_action(self, game):
        pass


class MovementCard(Card):

    def __init__(self, card_id, card_type, description, action_data):

        super().__init__(card_id, card_type, description, action_data)



class JailFree(Card):

    def __init__(self, card_id, card_type, description, action_data):

        super().__init__(card_id, card_type, description, action_data)

    def perform_action(self):
        pass

