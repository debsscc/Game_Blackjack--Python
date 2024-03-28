import random 
import time

#espadas, paus, copas e ouros 
naipes = "♠♣♥♦"
extras = "JQKA"
baralho = []

jogador = [] #cartas do jogador
pc = [] #cartas do pc

pontos_jogador = 0
pontos_pc = 0

def monta_baralho():
    for num in range (2,11):
        for naipe in naipes:
            baralho.append(str(num)+naipe)

    for extra in extras:
        for naipe in naipes:
            baralho.append(extra+naipe)

def pontos_carta(carta):
    if len(carta) == 3:
        return 10
    else:
        if carta[0].isdigit():
            return int(carta[0])
        elif carta[0] == "A":
            return 11
        else:
            return 10

monta_baralho()


contador = 1
contador_pc = 0

print("\nBem-vindo ao Blackjack! 🎩\n")


while True:
    num = random.randint(0,len(baralho)-1)
    carta = baralho.pop(num)

    peso = pontos_carta(carta)
    pontos_jogador += peso

    print(f"Sua {contador}ª Carta é: {carta}")
    time.sleep(2)

    contador += 1

    if contador >= 2:
        continua = input("Deseja receber outra carta? 🃏 (S/N) ").upper()
        if continua == "N":
            break

print(f"\n Total de Pontos do Jogador: {pontos_jogador}\n")
if pontos_jogador > 21:
    print("\033[1;31mBah, você perdeu a jogada de Blackjack.\033[m")
else:
    input("\nPressione Enter para Desafiar o Computador....\n")

while pontos_pc < 21:
    contador_pc += 1

    num = random.randint(0,len(baralho)-1)
    carta = baralho.pop(num)

    peso = pontos_carta(carta)
    pontos_pc += peso

    print(f"A {contador_pc}ª carta do computador 🖥 é: {carta}")
    time.sleep(2) 



print(f"\nTotal de Pontos do Computador: {pontos_pc}")

if pontos_pc > 21:
    print("\033[1;32mParece que você ganhou contra o computador!!🏆🏆\n")
    #\033[1;32m] torna o texto verde
elif pontos_pc == pontos_jogador:
    print("\033[1;33]Empatou!\n")
    #\033[1;33m] torna o texto amarelo
else:
    print("\033[1;31m]Jogada de mestre, a inteligência Annunaki ganhou de você.\n")
    #\033[1;31m] torna o texto vermelho

print("\033[0mObrigado por jogar Black Jack!🃏🃏\n")
# \033[0m] volta a cor do texto ao padrão
print("Volte Sempre!👋👋\n")
