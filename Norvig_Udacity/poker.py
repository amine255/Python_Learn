def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand, ...]"
    return allmax(hands, key=hand_rank) 
  
##############################################################################################################################  
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
      xval = key(x)
      if not result or xval > maxval:
        result, maxval = [x], xval
      elif xval == maxval:
        result.append(x)
    return(result)
  
## My Method:  
'''  
def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    m = max(iterable, key = key)
    li = []
    for it in iterable:
        if key(it) == key(m): 
            li += [it]
    return(li) 
 '''

##############################################################################################################################
# The hand_rank function returns the correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair, pair, and high card hands. 
#
# We assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has exactly n of. For A hand with 4 sevens  this function would return 7.
# two_pair(ranks): if there is a two pair, this function returns their corresponding ranks as a  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks in a hand (where the order goes from highest to lowest rank). 

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, max(ranks), min(ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2,ranks), ranks)
    else:                                          # high card
        return (0, ranks)  

##############################################################################################################################
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

## My Method:
'''  
def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [int(r.replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks
''' 

##############################################################################################################################
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

# My method:
'''
def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return((ranks[-1] - ranks[0] == 4) and (sum(ranks)/5 == ranks[2]))
'''

##############################################################################################################################  
def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return(len(set(suits)) == 1)

##############################################################################################################################  
def two_pair(ranks):
    "If there are two pair here, return the two ranks of the two pairs, else None."
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None

##############################################################################################################################  
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None  

## My Method:  
'''
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    if len(set(ranks)) == 5:
        if n != 1:
            return(None)
        else:
            return(ranks[0])
    elif len(set(ranks)) == 4:
        if n not in [1, 2]:
            return(None)
        elif n == 1:
            return(ranks[0]*(len(set(ranks[1:])) == 3) + ranks[2]*(len(set(ranks)) != 3))
        elif n == 2:
            for i in range(4):
                if (ranks[i] == ranks[i+1]):
                    return(ranks[i])
        else:
            return(None)
    elif len(set(ranks)) == 3:
        if n not in [1, 2, 3]:
            return(None)
        elif n == 1:
            if len(set(ranks[1:])) == 2:
                return(ranks[0])
            elif len(set(ranks[:3])) == 1:
                return(ranks[3])
            elif len(set(ranks [3:])) == 1:
                return(ranks[2])
            else:
                return(ranks[4])
        elif n == 2:
            if ranks[0] == ranks[1] and ranks[0] != ranks[2]:
                return(ranks[0])
            elif ranks[1] == ranks[2] and ranks[3] == ranks[4]:
                return(ranks[1])
        elif n == 3:
            if ranks[0] == ranks[1] and ranks[0] == ranks[2]:
                return(ranks[0])
            elif ranks[1] == ranks[2] and ranks[1] == ranks[3]:
                return(ranks[1])
            elif ranks[2] == ranks[3] and ranks[3] == ranks[4]:
                return(ranks[2])
        else:
            return(None)
    elif len(set(ranks)) == 2:
        if n not in [1, 2, 3, 4]:
            return(None)
        else:
            if n == 1:
                if ranks[0] != ranks[1]:
                    return(ranks[0])
                elif ranks[4] != ranks[3]:
                    return(ranks[4])
            elif n == 2:
                if ranks[0] == ranks[1] and ranks[1] != ranks[2]:
                    return(ranks[0])
                elif ranks[4] == ranks[3] and ranks[3] != ranks[2]:
                    return(ranks[3])
            elif n == 3:
                if ranks[0] == ranks[1] and ranks[1] != ranks[2]:
                    return(ranks[2])
                elif ranks[4] == ranks[3] and ranks[3] != ranks[2]:
                    return(ranks[0])
            elif n == 4:
                if ranks[0] == ranks[1] and ranks[2] == ranks[3]:
                    return(ranks[0])
                elif ranks[1] == ranks[2] and ranks[3] == ranks[4]:
                    return(ranks[1])
'''  

##############################################################################################################################
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert straight(card_ranks(al)) == True
    return 'tests pass'
  
  
  
##############################################################################################################################  
# Function, deal(numhands, n=5, deck), that deals numhands hands with n cards each.

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards.
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
  "Shuffle the deck and deal out numhands n-cards hands."
  random.shuffle(deck)
  return [deck[n*i:n*(i+1)] for i in range(numhands)]

# My method: Seems better in this case?
'''
def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    hands = []
    for i in range(numhands):
        hands.append(random.sample(mydeck, n))
    return(hands)
'''
  
