import random

class Card():

    def __init__(self):
        self.card_num = self.get_card_number()

    def get_card_number(self):
        return random.randint(1, 13)
