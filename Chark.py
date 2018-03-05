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
from Axe import Axe


class Chark(Player):

    def __init__(self, posx, posy, index, game):
        Player.__init__(self,100, 4, posx, posy, index, game)
        self.myString = "C" + str(index)
        self.equipment = Axe(self)

    def teleport(self):
        super(Chark, self).teleport()
        self.equipment.enhance()

    def askForMove(self):
        print("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)"
              % (self.index, self.equipment.getRange(), self.equipment.getEffect()))
        super(Chark, self).askForMove()
