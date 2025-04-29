""" The main menu system for how we can navigate what we need our algorithm to do
- Switch (match) case to """

import handstrength
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
roundNumber = 1
betFirst = False
numChips = 100
currentBet = 0

def OppBet():
    global roundNumber #idk i havent done python in forever. 

    print("Opponent Bet\n")
    print("0: call\n")
    print("1: raise\n")
    print("2: fold\n")
    dec = int(input("How did your opponent bet? "))
    
    if dec == 0: 
        print("Opponent called! Move to next round.")
        roundNumber+=1

    elif dec == 1: 
        print("Opponent raised!")
        user_input = int(input("Enter opponent bet: "))
        print("You entered:", user_input)
        if (user_input > currentBet):
            currentBet = user_input
        else:
            print("Raise amount was not greater than the current bet. ")
            OppBet()

    elif dec == 2: 
        print("Opponent folded, you win!")
        sys.exit()

def BetDecision(): 
    """check for initial bet, do not run"""
    if(betFirst == True): 

def InitBet(): 
    """ function that will tell us how much our bet should be at the beginning of each betting round """
    if(betFirst == True): 
        """ always bet 1 when we bet first """
        currentBet = 1
        numChips = numChips - currentBet
        print("Bet 1 chip\n")
    else:
        """ always call when opponent bets first """
        print("Call\n")



def main(): 
    """ menu logic """
    print("Game Stage Menu\n")
    print("0: Game Start\n")
    print("1: The Flop\n")
    print("2: The Turn\n")
    print("3: The River\n")
    print("4: Game End\n")
    
    opt_str = input("Enter the number that corresponds to the game stage you are in: ")
    opt = int(opt_str)

    """ https://www.geeksforgeeks.org/switch-case-in-python-replacement/ """
    match opt:
        case 0:
            # get number of chips from user
            numChips = int(input("Enter the number of chips you have to start this round: "))
            # get cards from user

            # who bets first?
            while(1)
            {
                first = input("Do you bet first? (y/n): ")
            if (first == "y" || first == "y " || first == "Y" || first == "Y "):
                betFirst = True
                InitBet()
                OppBet()
                break
            elif (first == "n" || first == "n " || first == "N" || first == "N "):
                betFirst = False
                currentBet = int(input("Enter opponent's initial bet: "))
                InitBet()
                break
            else:
                print("Invalid response. Try again.\n")
            }
            main()
            
        case 1:
            # do stuff
            revCard = input("Enter revealed cards.")
            if betFirst: #if true
                userInput = int(input("Enter opponent's move: 0-2 "))
                BetDecision()
                
            else: #if false 
                InitBet() 
                if(userInput == 0):
                    OppBet(0)
                elif(userInput == 1): 
                    OppBet(1)
                elif(userInput == 2): 
                    OppBet(2)    
            main()
            
        case 2:
            # do stuff
            main()
        case 3:
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
        case default:
            print("Invalid Menu Option\n")
            main()
            
            
