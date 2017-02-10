from random import randint
import numpy as np
import pylab as pl

class kellyCalc(object):
    def __init__(self,payout,winOdds):
        self.q = (1.0 - winOdds)
        self.b = payout
        self.p = winOdds
        
    def getFraction(self):
        fraction = (self.b*self.p - self.q)/self.b
        return fraction

## Set the odds at 
def genOutcome(odds):
    odds = float(odds)*100.0
    randomInt = float(randint(0,100))
    if(randomInt < odds):
        return 1
    else:
        return 0

def checkBet(bet,outcome):
    if(bet == outcome):
        return 'win'
    else:
        return 'loss'
    
def placeBet(bet,size,payout,odds):
    outcome = genOutcome(odds)
    result = checkBet(bet,outcome)
    if(result == 'win'):
        winnings = size + size*payout
    else:
        winnings = 0
    return winnings

def startGame():
    bankRoll = 1000.0
    payout = 1.0
    odds = .55
    kelly = kellyCalc(payout,odds)
    fraction = kelly.getFraction()
    winningBet = 1
    if(fraction < 0.0):
        print "Do Not Bet, Your Getting Fucked"
    else:
        x = []
        y = []
        for i in range(1000):
            betSize = bankRoll * fraction
            bankRoll = bankRoll - betSize
            winnings = placeBet(winningBet, betSize, payout, odds)
            bankRoll = winnings + bankRoll
            x.append(i)
            y.append(bankRoll)
        pl.plot(x,y)
        pl.show()
        

def main():
    startGame()

if __name__ == "__main__":
    main()
