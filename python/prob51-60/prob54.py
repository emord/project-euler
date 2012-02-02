#!/usr/python3

"""
In the card game poker, a hand consists of five cards and are ranked, from 
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest 
value wins; for example, a pair of eights beats a pair of fives (see example 1 
below). But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); if the 
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
Hand         Player 1         Player 2         Winner
1         5H 5C 6S 7S KD     2C 3S 8S 8D TD
Pair of Fives               Pair of Eights    Player 2

2         5D 8C 9S JS AC     2C 5C 7D 8S QH
Highest card Ace            Highest card Queen Player 1

3         2D 9C AS AH AC     3D 6D 7D TD QD
Three Aces                   Flush with Diamonds Player 2

4         4D 6S 9H QH QC     3D 6D 7H QD QS
Pair of Queens                Pair of Queens
Highest card Nine             Highest card Seven Player 1

5         2H 2D 4C 4D 4S     3C 3D 3S 9S 9D
Full House                     Full House
With Three Fours               with Three Threes Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the 
first five are Player 1's cards and the last five are Player 2's cards. You can 
assume that all hands are valid (no invalid characters or repeated cards), each 
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

import cProfile
from multiprocessing import Queue, Process

def isRoyalFlush(cards):
    suit = cards[0][1]
    values = { 'T', 'J', 'Q', 'K', 'A' }
    for card in cards:
        if card[1] != suit: return False
        if card[0] not in values: return False
        else: values.remove(card[0])
    return True

def isStraightFlush(cards):
    if isStraight(cards)[0] and isFlush(cards)[0]: 
        return (True, isStraight(cards)[1])
    else: return (False, '0')
    
def isFullHouse(cards):
    if isXOfAKind(cards, 3)[0] and isXOfAKind(cards, 2)[0]: 
        return (True, isXOfAKind(cards, 3)[1], isXOfAKind(cards, 2)[1])
    return (False, '0', '0')
    
def isFlush(cards):
    suits = set()
    for card in cards:
        suits.add(card[1])
        
    if len(suits) == 1: return (True, highestCard(cards))
    return (False, '0')

def isStraight(cards):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for card in cards:
        if card[0] not in values: return (False, '0')
        else: values[values.index(card[0])] = 'X'
        
    foundx = False
    consec = 0
    for value in values:
        if value == 'X':
            foundx = True
            consec += 1
        if value != 'X' and foundx: return (False, '0')
        if consec == 5: return (True, value)
        
def isXOfAKind(cards, x):
    y = dict()
    for card in cards:
        if card[0] not in y.keys(): y[card[0]] = 1
        else: y[card[0]] += 1
        
    for value in y.keys():
        if y[value] == x: return (True, value)
    
    return (False, '0')

def isTwoPairs(cards):
    values = [ ]
    dictvalues = dict()
    for card in cards:
        values.append(card[0])
        if card[0] not in dictvalues.keys(): dictvalues[card[0]] = 1
        else: dictvalues[card[0]] += 1
        
    a, b = 0, 0
    blah = False
    for x in dictvalues.keys():
        if dictvalues[x] == 2 and not blah:
            a = x
            blah = True
        elif dictvalues[x] == 2: b = x
        
    if set(values) != 3: return (False, '0')
    if not isXofAKind(cards,3)[0]: return (True, a, b)
    else: return(False, '0')
    
def highestCard(cards):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'][::-1]
    setcards = set()
    for card in cards:
        setcards.add(card[0])
    
    for value in values:
        if value in setcards: return value
    
def winner(player1, player2):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    if isRoyalFlush(player1) and not isRoyalFlush(player2): return 1
    elif isRoyalFlush(player2) and not isRoyalFlush(player1): return 2
    
    if isStraightFlush(player1)[0] and not isStraightFlush(player2)[0]: return 1
    elif isStraightFlush(player2)[0] and not isStraightFlush(player1)[0]: return 2
    elif isStraightFlush(player1)[0] and isStraightFlush(player2)[0]:
        if values.index(isStraightFlush(player1)[1]) > values.index(isStraightFlush(player2)[1]): return 1
        elif values.index(isStraightFlush(player2)[1])> values.index(isStraightFlush(player1)[1]): return 2
    
    if isXOfAKind(player1, 4)[0] and not isXOfAKind(player2, 4)[0]: return 1
    elif isXOfAKind(player2, 4)[0] and not isXOfAKind(player1, 4)[0]: return 2
    elif isXOfAKind(player1, 4)[0] and isXOfAKind(player2, 4)[0]:
        if values.index(isXOfAKind(player1, 4)[1]) > values.index(isXOfAKind(player2, 4)[1]): return 1
        elif values.index(isXOfAKind(player2, 4)[1]) > values.index(isXOfAKind(player1, 4)[1]): return 2
    
    if isFullHouse(player1)[0] and not isFullHouse(player2)[0]: return 1
    elif isFullHouse(player2)[0] and not isFullHouse(player1)[0]: return 2
    elif isFullHouse(player1)[0] and isFullHouse(player2)[0]:
        if values.index(isFullHouse(player1)[1]) > values.index(isFullHouse(player2)[1]): return 1
        elif values.index(isFullHouse(player2)[1]) > values.index(isFullHouse(player1)[1]): return 2
        if values.index(isFullHouse(player1)[2]) > values.index(isFullHouse(player2)[2]): return 1
        elif values.index(isFullHouse(player2)[2]) > values.index(isFullHouse(player1)[2]): return 2
        
    if isFlush(player1)[0] and not isFlush(player2)[0]: return 1
    elif isFlush(player2)[0] and not isFlush(player1)[0]: return 2
    elif isFlush(player1)[0] and isFlush(player2)[0]:
        if values.index(isFlush(player1)[1]) > values.index(isFlush(player2)[1]): return 1
        elif values.index(isFlush(player2)[1]) > values.index(isFlush(player1)[1]): return 2
        
    if isStraight(player1)[0] and not isStraight(player2)[0]: return 1
    elif isStraight(player2)[0] and not isStraight(player1)[0]: return 2
    elif isStraight(player1)[0] and isStraight(player2)[0]:
        if values.index(isStraight(player1)[1]) > values.index(isStraight(player2)[1]): return 1
        elif values.index(isStraight(player2)[1]) > values.index(isStraight(player1)[1]): return 2
    
    if isXOfAKind(player1, 3)[0] and not isXOfAKind(player2, 3)[0]: return 1
    elif isXOfAKind(player2, 3)[0] and not isXOfAKind(player1, 3)[0]: return 2
    elif isXOfAKind(player1, 3)[0] and isXOfAKind(player2, 3)[0]:
        if values.index(isXOfAKind(player1, 3)[1]) > values.index(isXOfAKind(player2, 3)[1]): return 1
        elif values.index(isXOfAKind(player2, 3)[1]) > values.index(isXOfAKind(player1, 3)[1]): return 2
        
    if isTwoPairs(player1)[0] and not isTwoPairs(player2)[0]: return 1
    elif isTwoPairs(player2)[0] and not isTwoPairs(player1)[0]: return 2
    elif isTwoPairs(player1)[0] and isTwoPairs(player2)[0]:
        if values.index(isTwoPairs(player1)[1]) > values.index(isTwoPairs(player2)[1]): return 1
        elif values.index(isTwoPairs(player2)[1]) > values.index(isTwoPairs(player1)[1]): return 2
        elif values.index(isTwoPairs(player1)[1]) == values.index(isTwoPairs(player2)[1]):
            if values.index(isTwoPairs(player1)[2]) > values.index(isTwoPairs(player2)[2]): return 1
            elif values.index(isTwoPairs(player2)[2]) > values.index(isTwoPairs(player1)[2]): return 2
    
    if not isTwoPairs(player1)[0] and not isTwoPairs(player2[0]):
        if isXOfAKind(player1, 2)[0] and not isXOfAKind(player2, 2)[0]: return 1
        elif isXOfAKind(player2, 2)[0] and not isXOfAKind(player1, 2)[0]: return 2
        elif not isTwoPairs(player1)[0] and not isTwoPairs(player2)[0] and isXOfAKind(player1, 2)[0] and isXOfAKind(player2, 2)[0]:
            if values.index(isXOfAKind(player1, 2)[1]) > values.index(isXOfAKind(player2, 2)[1]): return 1
            elif values.index(isXOfAKind(player2, 2)[1]) > values.index(isXOfAKind(player1, 2)[1]): return 2
        
    if values.index(highestCard(player1)) > values.index(highestCard(player2)): return 1
    elif values.index(highestCard(player2)) > values.index(highestCard(player1)): return 2
        
def worker(cards, out_q):
    player1wins = 0
    for game in cards:
        player1 = game.split()[:5]
        player2 = game.split()[5:]
        if winner(player1, player2) == 1: player1wins += 1
        
    out_q.put(player1wins)
        
def main():
    cards = open('prob54.dat').readlines()
    a = Queue()
    b = Queue()
    
    x = Process(target=worker, args=(cards[:len(cards)//2], a))
    y = Process(target=worker, args=(cards[len(cards)//2:], b))
    x.start()
    y.start()
    x.join()
    y.join()
        
    print(a.get() + b.get())
        
if __name__ == '__main__':
    cProfile.run('main()')