from card import Card
from random import Random

class Deck:
    free: list[Card]
    cards: list[Card]

    def __init__(self) -> None:
        for suit in Card.Suits:
            for number in Card.Values:
                self.free.append(Card(number, suit))
        for _ in range(5):
            self.cards.append(self.free.pop(Random().get_int_rand(len(self.free))))
    
    def switch(self, indexes: str) -> list[Card]:
        indexesList = indexes.split()
        for indexStr in indexesList:
            try:
                index = int(indexStr) - 1
            except ValueError:
                continue
            if index > len(self.cards):
                continue
            self.cards[index] = self.free.pop(Random().get_int_rand(len(self.free)))
        return self.cards
    
    def switchAll(self) -> list[Card]:
        for i in range(5):
            self.cards[i] = self.free.pop(Random().get_int_rand(len(self.free)))
        return self.cards
    
    def __str__(self) -> str:
        lines = []
        for i in range(6):
            lines[i] = ''
        for i, e in enumerate(self.cards):
            lines[0] += '+-----+ '
            lines[1] += '|     | '
            lines[2] += '| {}{} | '.format(e.number.name, e.suit.name)
            lines[3] += '|     | '
            lines[4] += '+-----+ '
            lines[5] += '  ({})   '.format(i)
        return '\n'.join(lines)