import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# use collections.namedtuple to construct a simple class to represent individual cards with just bundles of attributes and no custom methods.

class FrenchDeck:
 
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def display(self):
        for i in self._cards:
            print(i)
    
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    # this gives the index of the cards rank in the list [2,3,4,...J,Q]
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(rank_value)
    # we do rankvalue*4 because, each rank and card should have a unique range of values and shouldn't be affected by the suit addition.
    # Q(clubs) : 10 + 0, J(spades) : 9 + 3 = 12 which is wrong
    # Q        : 40,     J         : 39
    return rank_value*len(suit_values) + suit_values[card.suit]
def main():
    deck = FrenchDeck()
    # deck.display()
    # print(deck[41])
    for card in sorted(deck, key=spades_high):
        print(card)
    # print(len(deck))
    # print(deck[0])

if __name__ == "__main__":
    main()