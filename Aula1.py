print("--------------------")
print("teste de adivinhação")
print("--------------------")

numeroSecreto = 55

chute = int(input("chute algum numero "))
print("o numero dito foi ", chute)

if(chute==numeroSecreto):
    print("Você acertou")
else:
    print("Você errou")


