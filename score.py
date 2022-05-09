from card import Card

class Score:
    balance: int
    currentBet: int

    def __init__(self) -> None:
        self.balance = 200
        self.currentBet = 0
    
    def bet(self, amount: int) -> None:
        if not amount :
            raise Exception("Aposta precisa ser maior que 0")
        if amount > self.balance:
            raise Exception("Aposta não pode ser maior que saldo")
        self.currentBet = amount
        self.balance -= self.currentBet
    
    def pay(self, cards: list[Card]) -> int:
        cards.sort(key=lambda e: e.number.value)
        mult = 0
        if (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit) and (cards[0].number == Card.Values['10']) and (cards[1].number == Card.Values['J ']) and (cards[2].number == Card.Values['Q ']) and (cards[3].number == Card.Values['K ']) and (cards[4].number == Card.Values['A ']):
            mult = 200
        elif (cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit) and (cards[0].number.value == (cards[1].number.value - 1)) and (cards[1].number.value == (cards[2].number.value - 1)) and (cards[2].number.value == (cards[3].number.value - 1)) and (cards[3].number.value == (cards[4].number.value - 1)):
            mult = 100
        else:
            values = []
            for value in Card.Values:
                values.append([x.number for x in cards].count(value))
            if values.count(4) == 1:
                mult = 50
            elif (values.count(3) == 1) and (values.count(2) == 1):
                mult = 20
            elif cards[0].suit == cards[1].suit == cards[2].suit == cards[3].suit == cards[4].suit:
                mult = 10
            elif (cards[0].number.value == (cards[1].number.value - 1)) and (cards[1].number.value == (cards[2].number.value - 1)) and (cards[2].number.value == (cards[3].number.value - 1)) and (cards[3].number.value == (cards[4].number.value - 1)):
                mult = 5
            elif values.count(3) == 1:
                mult = 2
            elif values.count(2) == 2:
                mult = 1
        earnings = self.currentBet * mult
        self.balance += earnings
        self.currentBet = 0
        return earnings