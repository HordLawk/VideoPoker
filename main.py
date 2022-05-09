from score import Score
from deck import Deck

s = Score()
while s.balance:
    d = Deck()
    print("Saldo atual: ${}".format(s.balance))
    while True:
        valStr = input("Digite o valor da aposta ou 'F' para terminar ==> ")
        if valStr == "F":
            exit()
        try:
            betVal = int(valStr)
            try:
                s.bet(betVal)
                break
            except Exception as e:
                print(e)
        except:
            print("Valor deve ser um número ou 'F'")
    print(d)
    d.switch(input("Digite o número das cartas que você deseja trocar, separados por espaços: "))
    print(d)
    d.switch(input("Digite o número das cartas que você deseja trocar, separados por espaços: "))
    print(d)
    earnings = s.pay(d.cards)
    if earnings:
        print("Parabéns. Você acrescentou ${} ao seu saldo".format(earnings))
    else:
        print("Peninha... não ganhou nada nessa rodada")
    input("Tecle enter para continuar")
print("Seu saldo acabou")