import random

#create a deck class
class Deck:
  #create initial function
  def __init__(self):
    #Define list of card names
    cards = []
    suits = ["spades","clubs","hearts","diamonds"]
    
    #store ranks in a dictionary
    ranks = [
          {"rank":"A", "value":11},
          {"rank":"2", "value":2},
          {"rank":"3", "value":3},
          {"rank":"5", "value":5},
          {"rank":"6", "value":6},
          {"rank":"7", "value":7},
          {"rank":"8", "value":8},
          {"rank":"9", "value":9},
          {"rank":"10", "value":10},
          {"rank":"J", "value":10},
          {"rank":"Q", "value":10},
          {"rank":"K", "value":10}     
              ]
    
    #print each suit
    for suit in suits:
      for rank in ranks:
         #add the 52 cards to the list
        cards.append([suit, rank])
  
  
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
  

  
  