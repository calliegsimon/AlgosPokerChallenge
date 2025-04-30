""" The main menu system for how we can navigate what we need our algorithm to do
- Switch (match) case to """

import handstrength as hs
import sys 
import random 

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
oppChips = 100
currentBet = 0 
holeCards = ""
# round number doesnt matter because the menu option entered does this for us

def OppBet():
    global currentBet
    print("Opponent Bet\n")
    print("0: call\n")
    print("1: raise\n")
    print("2: fold\n")
    dec = int(input("How did your opponent bet? "))
    
    if dec == 0: 
        print("Opponent called! Move to next round.")
        # reset currentBet for next round
        currentBet = 0

    elif dec == 1: 
        print("Opponent raised!")
        user_input = int(input("Enter opponent bet: "))
        print("You entered:", user_input)
        
        # checking valid raise amount
        if (user_input > currentBet):
            currentBet = user_input
            # opponent raised, so we'll need to bet again
            BetDecision()
            
        else:
            print("Raise amount was not greater than the current bet. ")
            OppBet()

    elif dec == 2: 
        print("Opponent folded, you win!")
        sys.exit()

def BetDecision(): 
    global currentBet, numChips

    """check for initial bet, do not run"""
    if(betFirst == True): 
        print("stuff")


    #AFTER decision made -- AMY 
    print("Your Bet Options.. \n")
    print("0: call\n")
    print("1: raise\n")
    print("2: fold\n")

    userBet = int(input("enter what you want to do."))

    if userBet == 0: 
        print("you called! the current bet is .. ", currentBet)
        #move to next round 
    elif userBet == 1: 
        newBet = int(input("what are you raising to?"))
        OppBet(A)
        if A == 0: 
            print("call")
            #call 
        elif A == 1:
            print("raise") 
            #raise 
        elif A == 2: 
            print("fold")
            sys.exit()
            #fold 
    elif userBet == 2: 
        print("folded, end round")
        sys.exit()
        #end round, chips go to opponent (?)

def InitBet(): 
    global numChips, currentBet, betFirst
    """ function that will tell us how much our bet should be at the beginning of each betting round """
    if(betFirst == True): 
        """ always bet 1 when we bet first """
        currentBet = 1
        numChips = numChips - currentBet
        print("Bet 1 chip\n")
    else:
        """ always call when opponent bets first """
        numChips = numChips - currentBet
        print("Call\n")

def main(): 
    global numChips, holeCards, betFirst, currentBet, flopCards, riverCards, turnCards
    
    """ menu logic """
    print("Game Stage Menu\n")
    print("0: Game Start\n")
    print("1: The Flop\n")
    print("2: The Turn\n")
    print("3: The River\n")
    print("4: Game End\n")
    
    opt = int(input("Enter the number that corresponds to the game stage you are in: "))

    """ https://www.geeksforgeeks.org/switch-case-in-python-replacement/ """
    match opt:
        case 0:
            # get number of chips from user
            numChips = int(input("Enter the number of chips you have to start this game: "))
            # get cards from user
            userCards = input("Enter your cards. Separate cards by comma & space.\n")
            holeCards = tuple(userCards.split(", "))
            # who bets first?
            while 1:
                print("First Better\n")
                print("0: me\n")
                print("1: opponent\n")
                first = int(input("Who bets first?: "))
                match first:
                    case 0: 
                        betFirst = True
                        InitBet()
                        OppBet()
                        break
                    case 1:
                        betFirst = False
                        currentBet = int(input("Enter opponent's initial bet: "))
                        InitBet()
                        break
                    case _: #for some reason case default wasnt being accessed by PYLANCE - amy 
                        print("Invalid response. Try again.\n")
            main()
            
        case 1:
            revCard_flop = input("Enter 3 revealed cards. Separate cards by comma & space.\n")
            flopCards = tuple(revCard_flop.split(", "))
            # if you bet first, will do so for entire game
            if betFirst: 
                InitBet()
                OppBet()
            else:
                # inputting opponent's moves now happens in OppBet()
                OppBet()
                BetDecision()
            main()
            
        case 2:
            revCard_turn = input("Enter 1 revealed card. Separate cards by comma & space.\n")
            turnCards = tuple(revCard_turn.split(", "))
            # do stuff
            if betFirst:
                InitBet()
                OppBet()
            else:
                OppBet()
                BetDecision()
            main()
        case 3:
            revCard_river = input("Enter FINAL revealed card. Separate cards by comma & space.\n")
            riverCards = tuple(revCard_river.split(", "))
            if betFirst: #if true
                InitBet()
                OppBet()
            else:
                OppBet()
                BetDecision()
            # do stuff
            main()
        case 4: 
            print("No one folded. Time for everyone to reveal their hands.\n")
            print("Ranking of hands from best to worst:\n")
            print("- Royal Flush\n")
            print("- Straight Flush\n")
            print("- Four of a Kind\n")
            print("- Full House\n")
            print("- Flush\n")
            print("- Straight\n")
            print("- Three of a Kind\n")
            print("- Two Pair\n")
            print("- Pair\n")
            print("- High Card\n")
            sys.exit()
        case default:
            print("Invalid Menu Option\n")
            main()
# running program
main()