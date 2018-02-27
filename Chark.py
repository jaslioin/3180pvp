from Player import Player
from Axe import Axe


class Chark(Player):

    def __init__(self, posx, posy, index, game):
        super(Player, self).__init__(100, 4, posx, posy, index, game)

        self.myString = "C" + index
        self.equipment = Axe()

    def teleport(self):
        super(Player, self).__init__()
        self.equipment.enhance()

    def askForMove(self):
        print("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)"
              % (self.index, self.equipment.getRange(), self.equipment.getEffect()))
        super(Chark, self).askForMove()
