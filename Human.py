# CSCI3180 Principles of Programming Languages
# --- Declaration ---
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
# Assignment 2
# Name : Li Ho Yin
#Student ID : 1155077785
#Email Addr : hyli6@cse.cuhk.edu.hk
from Player import Player
from Rifle import Rifle


class Human(Player):
    def __init__(self, posx, posy, index, game):
        super(Human, self).__init__(80, 2, posx, posy, index, game)
        self.myString = 'H' + str(index)
        self.equipment = Rifle(self)

    def teleport(self):
        super(Human, self).teleport()
        self.equipment.enhance()

    def distance(self, posx, posy):
        pass

    def askForMove(self):
        print("You are a human (H%d) using Rifle. (Range %d, Ammo #: %d, Damage per shot: %d)"
              % (self.index, self.equipment.getRange(), self.equipment.getAmmo(),
                 self.equipment.getEffect()))
        super(Human,self).askForMove()
