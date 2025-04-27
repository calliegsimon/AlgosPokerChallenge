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
    "Royal Flush": 1,
    "Straight Flush": 2,
    "Four of a Kind": 3,
    "Full House": 4,
    "Straight": 6,
    "Three of a Kind": 7,
    "Two Pair": 8,
    "Pair": 9,
    "High Card": 10
}

def classifyHand(hand):
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
    """