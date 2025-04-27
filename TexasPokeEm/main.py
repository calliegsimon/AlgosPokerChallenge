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
    "main menu logic here"