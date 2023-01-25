print("--------------------")
print("teste de adivinhação")
print("--------------------")

numeroSecreto = 55

tentativas = 3
while(tentativas >0):
    print("tentativa: ", tentativas)
    chute = int(input("chute algum numero "))
    print("o numero dito foi ", chute)

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou, você chutou um número maior que o correto")
        if(menor):
            print("Você errou, você chutou um número menor que o correto")
    tentativas-=1


print("----Fim de jogo----")

