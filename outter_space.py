from player import Player
from human import Human
from ai import Ai

# strart first round

#  makes sure gesture and ties can be used

# if yes display round winner

#  continue to next round  (repeat steps 4-8)
#   
# if no rethrow (repeat steps 4-6)

#  display game winner after 3 rounds

class OutterSpace:

    def __init__(self) -> None:
        self.human = Human()
        self.ai = Ai()

    def display_welcome(self):
        input("Welcome to Outter Space, where the ultimate battle of Rock, Paper, Scissor, Lizard, Spock!")
        print()
        print()
        input("Here are the rules, you are not affriad of Spock's viporizing you!")
        print()
        print()
        input("Rock crushes Scissors, Scissors cut paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock")
    
    def player_selection(self, user_input):
        single_player = "Single player"
        Multiplayer = "Multiplayer"
        user_input == single_player
        user_input == Multiplayer
        user_input = input("Please select opponent: Single player or Multiplayer!")

    def run_game(self):
        self.display_welcome()
        self.player_selection(self.player_selection)
        self.game_play()
        self.display_winner()
    
    def game_play(self):
        # LIST OF WHAT BEATS WHAT:
        # rock -- scissors, lizard
        # paper -- rock, spock
        # scissors -- paper, lizard
        # lizard -- paper, spock
        # spock -- scissors, rock
        self.rounds = 0
        # while self.rounds <= 1:
        #     self.ai.throw_gesture()
        #     if self.player_selection() is :


            # conditional game jargon
            # rounds += 1
            # rounds == 3
        pass

    def display_winner(self):
        return Player()




# Theo & Mario made the dream work with the team work