from time import sleep
from card import Card
from game_common import Game_Common

class Card_Game():
    
    def __init__(self):
        self.common_data = Game_Common()
        self.name = input(str("What is your username/display name? "))
        print(f"Welcome to {self.common_data.game_name}, {self.name}!")

    def start_game(self):
        if self.ask_question("Would you like to play game (Y/N)? "):
            print("Great! Let's get started!")
            sleep(0.5)
            print("To play this game, you start with 300 point. \nA card will be picked. You will guess if the current card is higher or lower than the next one.\nYou earn 100 points if you guess right and loose 75 if you guess wrong.\n")
            sleep(0.5)
            print("Now... Shall we begin?")
            self.run_game()
        else:
            print("Come again soon! :)")
            sleep(1)
            exit(0)
        

    def run_game(self):
        self.card1 = self.draw_card()
        self.new_card = None
        while True:
            print(f"The current card is: {self.card1}")
            guess = input(int("Is the next card higher or lower than the previous card [h/l]? "))
            if guess in ["H".upper(), "HIGHER".upper()]:
                self.new_card = self.draw_card()
                if self.card1 > self.new_card:
                    print(self.common_data.get_encouragement())
                else:
                    print(self.common_data.get_wrong_choice())
            if guess in ["L".upper(), "LOWER".upper()]:    
                self.new_card = self.draw_card()
                if self.card1 < self.new_card:
                    print(self.common_data.get_encouragement())
                else:
                    print(self.common_data.get_wrong_choice())
    def draw_card(self):
        card = Card()
        return card.card_num

    def update_score(self):
        pass

    def ask_question(self, question):
        query = input(str(question))
        if query not in ["Y".upper(), "YES".upper(), "CONFIRM".upper()]:
            return True
        else:
            return False


if __name__ == "__main__":
    game = Card_Game()
    game.start_game()