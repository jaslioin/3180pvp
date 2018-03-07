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
from Human import Human
from Chark import Chark
from Player import Player
from Pos import Pos
from Obstacle import Obstacle
from Weapon import Weapon


class SurvivalGame(object):
    
    def __init__(self):
        self.D = 10
        self.O = 2
    def printBoard(self):
        printObject = [["  " for x in range(self.D)] for y in range(self.D)]

        i=0
        while(i<self.n):
            
            pos = self.teleportObjects[i].getPos()
            try:
                printObject[pos.getX()][pos.getY()] = \
                    self.teleportObjects[i].getName()
            except AttributeError:
                pass
            i += 1

        i=self.n
        while i<self.n+self.O :
            

            if isinstance(self.teleportObjects[i],Obstacle):

                pos = self.teleportObjects[i].getPos()
                tmp = i+1-self.n
                printObject[pos.getX()][pos.getY()] = 'O'+str(tmp)
            i += 1

        #print
        print " ",
        i=0
        while i<self.D:
            print("|  %d " % i),
            i += 1
        print("|")
        i=0
        while i < self.D*3.2 :
            print "-",
            i += 1
        print ""
        row=0
        while row < self.D:
            print row,
            col=0
            while col < self.D:
                print("| %s " %printObject[row][col]),
                col+=1
            print "|"
            i=0
            while i<self.D*3.2 :
                print "-",
                i+=1
            print ""
            row+=1

    def positionOccupied(self, randx, randy):
        for o in self.teleportObjects:
            if isinstance(o,Player):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return True
            else:
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return True
        return False

    def getPlayer(self, randx, randy):
        for o in self.teleportObjects:
            if isinstance(o,Player):
                pos = o.getPos()
                if pos.getX() == randx and pos.getY() == randy:
                    return o
        return None

    def init(self):
        print "Welcome to Kafustrok. Light blesses you. \n" \
              "Input number of players: (a even number)"
        self.n = int(raw_input())
        self.teleportObjects = [object() for x in range(self.n+self.O)]
        for i in range(0,self.n/2):
            #print "created ",i+1," entity"
            self.teleportObjects[i] = Human(0,0,i,self)
            self.teleportObjects[i+self.n/2] = Chark(0,0,i,self)            
        i= 0
        while(i<self.O):
            #print "created ",i," Obstacle"
            self.teleportObjects[i+self.n] = Obstacle(0,0,i,self)
            i += 1


    def gameStart(self):
        turn = 0
        numOfAlivePlayers = self.n

        while numOfAlivePlayers > 1:
            if turn == 0:
                for obj in self.teleportObjects :
                    obj.teleport()
                print "Everything gets teleported.."

            self.printBoard()

            if isinstance(self.teleportObjects[turn],Player):
                t = self.teleportObjects[turn]
                try:
                    if t.health > 0:
                        t.askForMove()
                        print ""
                except AttributeError:
                    pass
            turn = (turn + 1) % self.n

            numOfAlivePlayers = 0
            for i in range(0,self.n):
                if isinstance(self.teleportObjects[i],Player):
                    if self.teleportObjects[i].health > 0:
                        numOfAlivePlayers += 1

        print "Game over."
        self.printBoard()





game = SurvivalGame()
game.init()
game.gameStart()

