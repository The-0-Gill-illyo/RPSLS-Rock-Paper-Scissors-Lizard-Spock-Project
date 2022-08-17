from player import Player
import random
class Ai(Player):

    def __init__(self):
        super().__init__()
        self.gestures

    def throw_gesture(self):
        self.gesture = random.randint(self.gestures)

ai = Ai()
gesture_list = ai.gestures
print(gesture_list)