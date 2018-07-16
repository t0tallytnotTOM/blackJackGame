import random #<--------------- we need this to shuffle the deck of cards
def calcHand(hand):   # <--------- function for calculating the current value of a hand
    val = 0
    i = 0
    for c in hand:
        if c[0].isdigit() and c[1].isdigit():
            val += 10
        elif c[0].isdigit():
            val += int(c[0])
        elif c[0] == 'A':
            val += 11
            i += 1
        elif c[0] == 'J' or 'Q' or 'K':
            val += 10

    while val > 21 and i > 0:  # <--------- utilise the ability of the ace to be worth either 11 or 1
        val -= 10
        i -= 1
    return val

suits = ['\u2663','\u2660','\u2666','\u2665']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck = []
hand1 = []
hand2 = []

for s in suits:       #<-------------------  uses 2 loops to form a deck of cards
    for r in ranks:   #<--------
        p = ''
        p += r + s
        deck.append(p)

random.shuffle(deck)   #<---------- shuffle the deck of cards before playing
for i in range(2):     #<---------- deal each player 2 cards from the shuffled deck
    hand1.append(deck.pop())
    hand2.append(deck.pop())

hands = [hand1,hand2] #<--------- add the hands to a list in order to loop through them
i = 1
for h in hands:
    print('\n---PLAYER ' + str(i) + '---')
    for j in h:
        print(j)
    print(calcHand(h))
    hitMe = ''
    while hitMe != 'n' and calcHand(h) <= 21: #<------- ask the player if they want the 'hit me' option until they dont, or the value of their deck has reached 21
        if calcHand(h) == 21:
            break
        hitMe = input('Hit me! (y/n)')
        if hitMe == 'y':
            h.append(deck.pop())
            for j in h:
                print(j)
            print(calcHand(h))
    i += 1

if calcHand(hand1) > 21 and  calcHand(hand2) <= 21: #<------------ calculate the appropriate response based on both player's scores
    print('\nPLAYER 2 IS THE WINNER')
elif calcHand(hand2) > 21 and  calcHand(hand1) <= 21:
    print('\nPLAYER 1 IS THE WINNER')
elif calcHand(hand2) > 21 and  calcHand(hand1) > 21:
    print('\nYOU GUYS SUCK AT THIS GAME!')
else:
    if (21 - calcHand(hand1)) < (21 - calcHand(hand2)):
        print('\nPLAYER 1 IS THE WINNER')
    elif (21 - calcHand(hand1)) > (21 - calcHand(hand2)):
        print('\nPLAYER 2 IS THE WINNER')
    else:
        print('\nTIE, BOTH PLAYERS SCORED ' + str(calcHand(hand2)))