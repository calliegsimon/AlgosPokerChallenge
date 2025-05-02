""" Algorithms Texas Hold'em Program
Group Members
- Callie Simon
- Abby Wenger
- Amy Nguyen
"""

""" The main menu system for how we can navigate what we need our algorithm to do
- Switch (match) case to """

import handstrength as hs
import sys 
import random 
import math

""" when entering in input cards add output lines for how to enter cards.

    Here is the output to be displayed:
    
    print("Enter your cards!\n")
    print("The value of a card is the first letter, followed by a lowercase suit letter.\n")
    print("spades = s\n" 
    "diamonds = d\n" 
    "hearts = h\n" 
    "clubs = c\n" 
    "For example 4 of hearts is 4h.\n")"""

#global variables that you can change if u want 
betFirst = False
numChips = 100 # will need to update this when we call/raise
currentBet = 0
additionalBet = 0
opponentBet = 0
holeCards = ""
flopCards = ""
turnCards = ""
riverCards = ""
rnd = 0 # round number for use in BetDecision()
bluff = False

def Bluff():
    """ function to determine if we should bluff this game 
        - should only be called on game start phase """

    global bluff

    result = random.randint(1,10)
    # bluff if result == 5 or 10 (will bluff about 20% of the time)
    if ((result == 5) or (result == 10)):
        bluff = True
    else:
        bluff = False

def OppBet():
    global currentBet, opponentBet, additionalBet, rnd

    print("Opponent Bet")
    print("0: call")
    print("1: raise")
    print("2: fold")
    dec = int(input("How did your opponent bet? "))
    
    if dec == 0: 
        print("Opponent called! Move to next round.")
        # no need to set opponentBet since we're moving to next round
        # reset currentBet for next round
        currentBet = 0

    elif dec == 1: 
        print("Opponent raised!")
        opponentBet = int(input("Enter opponent bet: "))
        
        # checking valid raise amount
        if (opponentBet > currentBet):
            # additionalBet is amount of chips to add if we call after opponent raise
            additionalBet = opponentBet - currentBet
            currentBet = opponentBet
            # opponent raised, so we'll need to bet again
            BetDecision(rnd, True)
            
        else:
            print("Raise amount was not greater than the current bet. ")
            OppBet()

    elif dec == 2: 
        print("Opponent folded, you win!")
        sys.exit()

def BetDecision(rnd, oppRaise): 
    """ function to decide if user should call, bet, or fold
        - this function should be called after opponent has made initial bet 
          or has raised our bet """

    # oppRaise == True if being called from OppBet
    # oppRaise == False if being called from InitBet (opponent has just made the initial bet)

    global flopCards, turnCards, riverCards, holeCards, numChips, currentBet, bluff, opponentBet

    myBet = 0 # storing how many chips to put into pot

    match rnd:
        case 0:
            tableCards = []
        case 1:
            tableCards = flopCards
        case 2:
            tableCards = flopCards + turnCards
        case 3:
            tableCards = flopCards + turnCards + riverCards

    tableCards = tuple(tableCards)
    holeCards = tuple(holeCards)
    # never fold if bestHand >= 3
    bestHand = hs.highest_possible_hand(holeCards, tableCards)
    p_pot, n_pot = hs.hand_potential(holeCards, tableCards)
    current_hs = hs.hand_strength(holeCards, tableCards)
    ehs = hs.EHS(current_hs, n_pot, p_pot) # on last round p_pot & n_pot = 0, so ehs = current_hs
    
    # check that we have enough chips to cover currentBet
    if (numChips <= currentBet):
        # must go all in or fold
        if (ehs < 0.4):
            # go all in
            userBet = 3
        else:
            # fold
            userBet = 2
    # decision if we are bluffing
    elif (bluff == True):
        # when "bluffing" won't fold & lower threshold for raising
        # because of how this is set up, we could still have a good hand when we are bluffing
        if (ehs > 0.2):
            # raise
            userBet = 1

            # calculate how much to raise
            if (ehs > 0.3):
                # 2x currentBet
                # check that we have enough to bet that much and still have something left
                if (oppRaise == True):
                    # if opponent raised, we need to compare amounts to additionalBet & currentBet
                    if (numChips > math.floor(1.75*currentBet + additionalBet)):
                        currentBet = math.floor(1.75*currentBet)
                        myBet = currentBet + additionalBet
                    elif (numChips > math.floor(1.25*currentBet + additionalBet)):
                        currentBet = math.floor(1.25*currentBet)
                        myBet = currentBet + additionalBet
                    else:
                        # call instead
                        userBet = 0
                        # opponent raised, so I only need to add the difference between my last bet and theirs
                        myBet = currentBet - additionalBet
                else:
                    if (numChips > math.floor(1.75*currentBet)):
                        currentBet = math.floor(1.75*currentBet)
                        myBet = currentBet
                    elif (numChips > math.floor(1.25*currentBet)):
                        currentBet = math.floor(1.25*currentBet)
                        myBet = currentBet
                    else:
                        # call instead
                        userBet = 0
                        myBet = currentBet
            else:
                # 1.25x currentBet
                # check that we have enough to bet that much and still have something left
                if (oppRaise == True):
                    if (numChips > math.floor(1.25*currentBet + additionalBet)):
                        currentBet = math.floor(1.25*currentBet)
                        myBet = currentBet + additionalBet
                    else:
                        # call instead
                        userBet = 0
                        # opponent raised, so I only need to add the difference between my last bet and theirs
                        myBet = additionalBet
                else:
                    if (numChips > 1.25*currentBet):
                        currentBet = math.floor(1.25*currentBet)
                        myBet = currentBet
                    else:
                        # call instead
                        userBet = 0 
                        myBet = currentBet              
        else:
            # call
            userBet = 0
            if (oppRaise == True):
                myBet = currentBet - additionalBet
            else:
                myBet = currentBet
    
    # decision if we are not bluffing
    else:
        # decision purely based off calculations
        if (ehs > 0.3):
            # raise
            userBet = 1

            # calculate how much to raise
            if (ehs > 0.5):
                # 2x currentBet
                # check that we have enough to bet that much and still have something left
                if (oppRaise == True):
                    if (numChips > math.floor(2*currentBet + additionalBet)):
                        currentBet = math.floor(2*currentBet)
                        myBet = currentBet + additionalBet
                    elif (numChips > math.floor(1.5*currentBet + additionalBet)):
                        currentBet = math.floor(1.5*currentBet)
                        myBet = currentBet + additionalBet
                    else:
                        # call instead
                        userBet = 0
                        # opponent raised, so I only need to add the difference between my last bet and theirs
                        myBet = additionalBet
                else:
                    if (numChips > math.floor(2*currentBet)):
                        currentBet = math.floor(2*currentBet)
                        myBet = currentBet
                    elif (numChips > math.floor(1.5*currentBet)):
                        currentBet = math.floor(1.5*currentBet)
                        myBet = currentBet
                    else:
                        # call instead
                        userBet = 0
                        myBet = currentBet

            else:
                # 1.5x currentBet
                # check that we have enough to bet that much and still have something left
                if (oppRaise == True):
                    if (numChips > math.floor(1.5*currentBet + additionalBet)):
                        currentBet = math.floor(1.5*currentBet)
                        myBet = currentBet + additionalBet
                    else:
                        # call instead
                        userBet = 0
                        # opponent raised, so I only need to add the difference between my last bet and theirs
                        myBet = currentBet - additionalBet
                else:
                    if (numChips > 1.5*currentBet):
                        currentBet = math.floor(1.25*currentBet)
                        myBet = currentBet
                    else:
                        # call instead
                        userBet = 0 
                        myBet = currentBet

        elif (ehs > 0.1):
            # call
            userBet = 0
            if (oppRaise == True):
                myBet = currentBet - additionalBet
            else:
                myBet = currentBet

        else:
            # fold if we don't have strong hand
            if (bestHand < 3):
                userBet = 2
            else:
                # if we should fold by calculations, but we have a good hand, just call
                userBet = 0
                if (oppRaise == True):
                    myBet = currentBet - additionalBet
                else:
                    myBet = currentBet

    if userBet == 0: 
        # call
        print("You should CALL. Match the current bet of ", currentBet, ".")
        if (oppRaise == True):
            print("Opponent raised by", additionalBet, ", so you should bet a total of", myBet, "chips.")
        else:
            print("Opponent's initial bet was", opponentBet, "chips, so you should bet the same.")
        numChips = numChips - myBet
        print("You should have", numChips," chips remaining.")
        currentBet = 0
        #move to next round
    elif userBet == 1: 
        # raise
        print("You should RAISE bet to", currentBet, "chips.\n")
        if (oppRaise == True):
            print("Opponent raised by", additionalBet, ", so you should bet a total of", myBet, "chips.")
        else:
            print("Opponent's initial bet was", opponentBet, "chips, so you should bet a total of", myBet, "chips.")
        numChips = numChips - myBet
        print("You should have", numChips, "chips remaining.\n")
        OppBet()
        # see how opponent wants to proceed
    elif userBet == 2: 
        # fold
        print("You should FOLD. Sorry, you lose!\n")
        sys.exit()
        #end round, chips go to opponent
    elif userBet == 3:
        # going all in, no need to bet anymore
        print("CALL what you can - bet all your chips.\n")
        print("Flip over any remaining cards and see who wins.\n")
        sys.exit()

def InitBet(): 
    """ function that will tell us how much our bet should be at the beginning of each betting round """

    global numChips, currentBet, betFirst, rnd, opponentBet

    if(betFirst == True): 
        """ always bet 1 when we bet first """
        currentBet = 1
        numChips = numChips - currentBet
        print("Bet 1 chip")
        print("You should have", numChips, "chips remaining.\n")
        OppBet()
    else:
        """ get opponent's initial bet, and then make a decision about how to proceed"""
        opponentBet = int(input("Enter opponent's initial bet: "))
        if opponentBet == 0:
            # if opponent didn't bet anything start the betting at 1
            currentBet = 1
            numChips = numChips - currentBet
            print("RAISE bet to 1 chip\n")
            print("You should have", numChips, "chips remaining.\n")
            OppBet()

        else:
            currentBet = opponentBet
            BetDecision(rnd, False)

def main():
    """ menu logic """
    global numChips, holeCards, flopCards, turnCards, riverCards, betFirst, currentBet, rnd

    print("\n")
    print("Game Stage Menu")
    print("0: Game Start")
    print("1: The Flop")
    print("2: The Turn")
    print("3: The River")
    print("4: Game End")
    
    opt = int(input("Enter the number that corresponds to the game stage you are in: "))

    """ https://www.geeksforgeeks.org/switch-case-in-python-replacement/ """
    match opt:
        case 0:
            rnd = 0

            # bluff?
            Bluff()

            # get number of chips from user
            numChips = int(input("Enter the number of chips you have to start this game: "))
            
            # get cards from user
            userCards = input("Enter your cards. Separate cards by comma & space.\n")
            holeCards = tuple(userCards.split(", "))
            
            # who bets first?
            while 1:
                print("First Better")
                print("0: me")
                print("1: opponent")
                first = int(input("Who bets first?: "))
                match first:
                    case 0: 
                        betFirst = True
                        break
                    case 1:
                        betFirst = False
                        break
                    case _: #for some reason case default wasnt being accessed by PYLANCE
                        print("Invalid response. Try again.\n")
            InitBet()
            main()
            
        case 1:
            rnd = 1
            revCard_flop = input("Enter 3 revealed cards.\n")
            flopCards = tuple(revCard_flop.split(", "))
            InitBet()
            main()
            
        case 2:
            rnd = 2
            revCard_turn = input("Enter 1 revealed card.\n")
            turnCards = tuple(revCard_turn.split(", "))
            InitBet()
            main()
        case 3:
            rnd = 3
            revCard_river = input("Enter FINAL revealed card.\n")
            riverCards = tuple(revCard_river.split(", "))
            InitBet()
            main()
        case 4: 
            rnd = 4
            print("No one folded. Time for everyone to reveal their hands.\n")
            print("Ranking of hands from best to worst: ")
            print("- Royal Flush")
            print("- Straight Flush")
            print("- Four of a Kind")
            print("- Full House")
            print("- Flush")
            print("- Straight")
            print("- Three of a Kind")
            print("- Two Pair")
            print("- Pair")
            print("- High Card")
            sys.exit()
        case _:
            print("Invalid Menu Option")
            main()

# running program
main()
