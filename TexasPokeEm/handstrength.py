"""
This file we handle all things necessary for our EHS (effective hand implementations)
Notes:
- handRanks = a dictionary of hand ranks for easy lookup
- 
"""

from itertools import combinations

#dictionary to store hand ranks needed for EHS
# referenced from: https://www.kaggle.com/datasets/camillahorne/poker-hands?select=ranked_poker_hands.csv
# ^ they also have all the possible permutations
handRanks = {
    #EHS needs handranks sorted weakest to strongest, ie strongest rank has highest val
    9 : "Royal Flush",
    8 : "Straight Flush",
    7 : "Four of a Kind",
    6 : "Full House",
    5 :"Flush",
    4 : "Straight",
    3 : "Three of a Kind",
    2 : "Two Pair",
    1: "Pair",
    0: "High Card"
}

# we are going to assign card ranks to values for ease of comparison.
# global!
rankValues = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def type_hand(ourHand):
    """ this is a util function that will assign the hand type based on a string of hands.
    For an example, I liked how the dataset linked above, camillahorne's, we about representing cards.
    
    Quoted from dataset description:
    All possible poker hands
    The dataset all_possible_poker_hands.csv is a dataset of every,
     possible card combination for a poker hand.
    The hand column is ordered from A to 2 just as the previous dataset.
    The suitedCards column is ordered from A to 2, while the suit,
     order is hearts, spades, diamonds, and clubs. The value of a card is the first letter,
     followed by the first letter of the suit. E.g. Jack of diamonds is Jd.
     
    Suits will always be lowercase for readibility.

    input: ourHand - array of cards
            card - each card in the array is represented by the two letter scheme above
    return: the rank of the hand
    """
    # separate the card ranks & suits
    # Jd 
    # card[0] = J
    # card[1] = 1
    cardRanks = [card[0] for card in ourHand]
    cardSuits = [card[1] for card in ourHand]

    # sort the ranks for each of our card's ranks
    sortedCardRanks = sorted([rankValues[i] for i in cardRanks], reverse=True)

    #count the frequency of ranks & suits
    rankCnt = {}
    for i in cardRanks:
        #https://www.geeksforgeeks.org/python-dictionary-get-method/
        rankCnt[i] = rankCnt.get(i, 0) + 1
    
    suitCnt = {}
    for j in cardSuits:
        suitCnt[j] = suitCnt.get(j, 0) + 1
    
    # here we are going to being doing our card checks. 

    # https://docs.python.org/3/library/functions.html#any
    # using any we are going to check if there are 5 of any suit in suitCnt
    flush = any(cnt == 5 for cnt in suitCnt.values())

    # checking for straight
    #https://docs.python.org/3/tutorial/controlflow.html
    straight = False
    if sortedCardRanks == [14, 5, 4, 3, 2]:
        straight = True
    else:
        # iterate 
        for i in range(len(sortedCardRanks) - 1):
            if sortedCardRanks[i] - sortedCardRanks[i+1] != 1:
                break
        else:
            straight = True

    # checking for royal flush
    if flush and straight and max(sortedCardRanks) == 14:
        return 9
    
    # check for straight flush
    if flush and straight:
        return 8
    
    # checking four of a kid
    if 4 in rankCnt.values():
        return 7
    
    #checking for full house 
    if 3 in rankCnt.values() and 2 in rankCnt.values():
        return 6
    
    # checking for just a normal flushj
    if flush: 
        return 5
    
    if straight:
        return 4
    
    if 3 in rankCnt.values():
        return 3 
    
    #checking for a two pair 
    pair = list(rankCnt.values()).count(2)
    if pair == 2:
        return 2
    
    if pair == 1:
        return 1

    # returning high card as the else
    return 0

def highest_possibleHand(ourCards, tableCards):
    """ Evaluating the best possible hand out of the combinations of allCards """
    allCards = ourCards + tableCards
    bestPoss = 0

    # going through all possible combos of all 



def EHS(curr_hs, n_pot,p_pot):
    """ EHS is the effective hand strength algo. 
    We are going to implement Billing's et. al's effective hand strength algorithm
    in order to assess how good our hand is and judge decisions after that.
    - numerical approach to quantify the strength of a poker hand,
     where its result expresses the strength of a hand in percentile (0-1),
     compared to all other possible hands.
    
    Parameters:
    - curr_hs - current hand strength (does not account for the potential to
      improve or deteiorate.  
    - n_pot - negative potential, probability that it gets worse and becomes a losing hand
    - p_pot - positive potential, probability it can improve and becomes the winning hand
    
    """
    ehs = curr_hs * (1 - n_pot) + (1 - curr_hs) * p_pot

    return ehs

def hand_strength(ourCards, tableCards,oppCards): 
    """ HS enumerates all possible opponent hand cards and counts the occurrneces where 
    ours is the strongest (+50 of cases where we are tied) 
    
    Pseudocode from paper:
    HandStrength(ourcards,boardcards)
    { ahead = tied = behind = 0
    ourrank = Rank(ourcards,boardcards)
    /* Consider all two card combinations of */
     /* the remaining cards. */
     for each case(oppcards)
        {   opprank = Rank(oppcards,boardcards)
            if(ourrank>opprank)  ahead += 1
        else if(ourrank=opprank) tied += 1
        else /* < */ behind += 1
        }
    handstrength = (ahead+tied/2)
     (ahead+tied+behind)
    return(handstrength)
    """
    ahead, behind, tied = 0

    ourRank = rank_hand(ourCards, )

def hand_potential(ourCards, tableCards, oppCards):