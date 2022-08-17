from player import Player
class Human(Player):

    def __init__(self):
        super().__init__()
        self.gestures

    def throw_gesture(self):
        self.user_gestsure = input('Choose one geture: Rock, Paper, Scissors, Lizard, Spock.')


user = Human()
gesture_list = user.gestures
print(gesture_list)

user_gesture = Human()
chosen_gesture = user_gesture.throw_gesture # Figure out how to catch user imput in chosen gesture
print(chosen_gesture)  