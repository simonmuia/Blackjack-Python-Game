import random

#Define list of card names
cards = []
suits = ["spades","clubs","hearts","diamonds"]

#store ranks in a dictionary
ranks = [
        
          ]

#print each suit
for suit in suits:
  for rank in ranks:
    cards.append([suit, rank[0]]) #add cthe 52 cards to the list


#Shuffle cards
def shuffle():
  random.shuffle(cards)

#after shuffle, pop a card
def deal(number):
  cards_dealt = [] #return a list of cards dealt
  for x in range(number):
    card = cards.pop()
    cards_dealt.append(card) #add popped cards to the cards_dealt list
  return cards_dealt

shuffle()

#store both rank name and value in a linked list
#create first card and store it outside card deck
card = deal(1)[0]


