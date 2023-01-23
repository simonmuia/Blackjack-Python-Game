import random

class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
    #print the card name in a string
  def __str__(self):
    return f" {self.rank['rank']}  of {self.suit}"

#create a deck class
class Deck:
  #create initial function
  def __init__(self):
    #Define list of card names
    self.cards = []
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
        self.cards.append(Card(suit, rank))
  
  
  #Shuffle cards
  def shuffle(self):
    if len(self.cards) > 1:
      random.shuffle(self.cards)
  
  #after shuffle, pop a card
  def deal(self, number):
    cards_dealt = [] #return a list of cards dealt
    for x in range(number):
      if len(self.cards) > 0:
        card = self.cards.pop()
        #add popped cards to the cards_dealt list
        cards_dealt.append(card) 
    return cards_dealt


class Hand:
  def __init__(self, dealer=False):
    self.cards = []
    self.value = 0
    self.dealer = dealer
  def add_card(self, card_list):
    self.cards.extend(card_list)
  #calculate value of cards in hands
  def calculate_value(self):
    self.value = 0
    has_ace = False
    
    for card in self.cards:
      card_value = int(card.rank["value"])
      self.value+= card_value
      #check if card has ace and if value is True

      if has_ace and self.value > 21:
        self.value -=10

  def get_value(self):
    self.calculate_value()
    return self.value

  def is_blackjack(self):
    return self.get_value()== 21

  
  def display(self,show_all_dealer_cards=False):  
    print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
    #get index and card
    for index, card in enumerate(self.cards):
      if index==0 and self.dealer \
      and not show_all_dealer_cards and not self.is_blackjack():
        print("hidden")
      else:
        print(card)
      
    if not self.dealer:
      print("Value: ", self.get_value())

class Game:
  