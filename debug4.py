# GoFishBuggy -- a buggy Go Fish Game
# reference: Adam Barr, Find the Bug
import random
def getCard(deck):
	""" Randomly remove a single card from the deck and return it. Assumes deck is not empty
	"""
	index = int(len(deck)*random.random())
	newCard= deck[index]
	del deck[index]
	return newCard

def drawCard(name,deck,hand):
	""" Draw a new card from the deck and add it to hand. If the hand now holds the rank in 
	all four suits, remove them from the hand
	"""
	if len(deck) > 0: # non-empty deck
		newCard = getCard(deck)
		cardRank = newCard[0]
		cardSuit=newCard[1]

		if cardRank in hand:
			hand[cardRank].append(cardSuit)
			if len(hand) == 4:
				print(name + " lay down " + cardRank + "s")
				del hand[cardRank]
			else:
				hand[cardRank] = [ cardSuit ]

def checkCard( handName, playerHand,cardRank, opponentHand):
	"""Check if opponentHand contains any cards of this specified rank.. If so, transfer
	to playerHand

	Returns 1 if a card transferred, 0 otherwise
	"""
	if cardRank in opponentHand:
		transferCards = opponentHands[cardRank]
		#transferCards is a ist
		del opponentHand[cardRank]
		if cardRank in playerHand:
			playerHand[cardRank].extend(transferCards)
		else:
			playerHand[cardRank] = transferCards

		if len(playerHands[cardRank])==4:
			print(handName+" lay down ", cardRank +"s")
			del playerHand[cardRank]
			return 1
		else:
			return 0

def doTurn(handName, deck, playerHand, opponentHand):
	""" play one turn of Go Fish:
	- a rank in playerHand is chosen and 
	- if any cards of that rank exist in opponentHand
	- they are transferred
	- This continues until no cards are transferred at which point
	- a card is drawn from the deck
	"""

	while len(playerHand):
		index = int(len(playerHand)* random.random())
		rankToCheck = playerHand.keys()[index]
		found=checkCard(handName,opponentHand, rankToCheck, playerHand)
		if found==0:
			break
	
	drawCard(handName, deck, playerHand)

ranks = ["2","3", "4", "5", "6", "7", "8", "9", "10", "J",  "Q", "K", "A"]
suits = [ "spades", "hearts", "diamonds", "clubs"]

def playGoFish():
	print("hello")
	deck=[]
	hand1={}
	hand2={}
	for i in range(52):
		deck.append((ranks[i%13],suits[i%4]))

	for i in range(7):
		drawCard("HAND1", deck, hand1)
		drawCard("HAND2", deck, hand2)

	while 1:
		doTurn("HAND1",deck, hand1, hand2)
		doTurn("HAND2", deck, hand2, hand1)
		if len(hand1)==0 and len(hand2)==0:
			break


playGoFish()