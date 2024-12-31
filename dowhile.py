"""

do while

código  apra advinhar um número

"""

palpite = 0
numero = 9

while True:
    print("Qual o número correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns você acertou o número")
        break
    else:
        print("Você errou. Tente novamente!")
else:
    print("Erro na aplicação")
    print(bool(palpite))
