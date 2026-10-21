class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __len__(self):
        return len(self._cards)


suits = "spades diamonds clubs hearts".split()
ranks = [str(n) for n in range(2, 11)] + list("JQKA")
i = 0
for suit in suits:
    for rank in ranks:
        card = Card(suit, rank)
        j = i + 1
        print(f"{"Card"} {j}")
        print("-----")
        print(f"{"Rank"} : {card.rank}")
        print(f"{"Suit"} : {card.suit}")
        print("")
        ##  print(f"{j}. {card.rank} of {card.suit}")
        i += 1

print("The total number of cards is : ", i)
        
        



