import random
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def displayInfo(self):
        print "You have", self.value, "of", self.suit
        return self

class Deck(object):
    def __init__(self):
        self.content = []
    def createCard(self):
        suits = ["hearts", "clubs", "spades", "diamonds"]
        values = [2,3,4,5,6,7,8,9,10, "Jack", "Queen", "King", "Ace"]
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.content.append(card)
    def displayDeck(self):
        for card in self.content:
            print card.value, "of", card.suit
        return self
    def shuffle(self):
        random.shuffle(self.content)
        return self
    def dealCards(self, number):
        cardlist = []
        for i in range (0, number):
            card1 = self.content.pop()
            cardlist.append(card1)
        for card in cardlist:
            print card1.value, "of", card1.suit

deck1 = Deck()
deck1.createCard()
deck1.displayDeck().shuffle().displayDeck()
print deck1.dealCards(3)
print len(deck1.content)

# Alternate method for shuffle:
    # for card in self.content:
    #     start = random.randrange(0,len(self.content))
    #     end = random.randrange(0, len(self.content))
    #     temp = self.content[start]
    #     self.content[start] = self.content[end]
    #     self.content[end] = temp
