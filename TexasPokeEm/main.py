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
numChips = 10 

def OppBet(dec):
    global roundNumber #idk i havent done python in forever. 

    if dec == 0: 
        print("opponent called! move to next round.")
        roundNumber+=1

    elif dec == 1: 
        print("opponent raised!")
        user_input = int(input("Enter opponent bet: "))
        print("You entered:", user_input)

    elif dec == 2: 
        print("opponent folded, you win!")
        sys.exit()

def BetDecision(): 
    "check for initial bet, do not run"
    if(betFirst == True): 

def InitBet(): 
    " function that will tell us how much our bet should be at the beginning of each betting round "
    if(betFirst == True): 



def main(): 
    print("Game Stage Menu\n")
    print("0: Game Start\n")
    print("1: The Flop\n")
    print("2: The Turn\n")
    print("3: The River\n")
    print("4: Game End\n")
    
    opt_str = input("Enter the number that corresponds to the game stage you are in: ")
    opt = int(opt_str)

    match opt:
        case 0:
            # do stuff
            main()
        case 1:
            # do stuff
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
            
            
