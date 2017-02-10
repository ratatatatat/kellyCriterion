class deckObj(object):
    def __init__(self):
        self.deck = self.genDeck()

    def genDeck(self):
        preDeck = []
        index = 0
        for i in range(52):
            valueIndex = i%13
            value = str(valueIndex)
            suitIndex = i /13
            card = {}
            if( suitIndex == 0 ):
                suit = 'Spade'
            if( suitIndex == 1 ):
                suit = 'Heart'
            if( suitIndex == 2 ):
                suit = 'Club'
            if( suitIndex == 3 ):
                suit = 'Diamond'
            if( valueIndex == 0):
                value = 'A'
            if( valueIndex == 10 ):
                value = 'J'
            if( valueIndex == 11 ):
                value = 'Q'
            if( valueIndex == 12 ):
                value = 'K'
            card['value'] = value
            card['suit'] = suit
            preDeck.append(card)
        deck = []
        return preDeck
    
    def getDeck(self):
        return self.deck


def main():
    deck = deckObj()
    print str(len(deck.getDeck()))
    print deck.getDeck()

if __name__ == "__main__":
    main()
                
