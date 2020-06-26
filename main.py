import random  # used for shuffling cards

print("Hello, world!")

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")
    

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(2, 15):
                if value == 11:
                    value = "Jack"
                elif value == 12:
                    value = "Queen"
                elif value == 13:
                    value = "King"
                elif value == 14:
                    value = "Ace"
                self.cards.append(Card(suit, value))

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for card in self.cards:
            card.show()


class Player:
    def __init__(self):
        pass

deck = Deck()
deck.shuffle()
deck.show()