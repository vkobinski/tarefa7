from random import randint
import os
import time

palavras = []

with open("./palavras.txt", 'r') as arquivo:
    for palavra in arquivo:
        palavras.append(palavra.replace('\n', ''))

palavra_escolhida = randint(0, len(palavras)-1)
palavra_escolhida = palavras[palavra_escolhida]
palavra_escolhida_teste = palavra_escolhida

palavra = []

for letra in palavra_escolhida:
    palavra.append(letra)

for i in range(len(palavra_escolhida)-2):
    escolha_1 = randint(0, len(palavra)-1)
    escolha_2 = randint(0, len(palavra)-1)
    letra1 = palavra[escolha_1]
    palavra[escolha_1] = palavra[escolha_2]
    palavra[escolha_2] = letra1


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear_screen()
print("---------------------------------------------------------------------------------------")
print("|Seja Bem-Vindo ao jogo de adivinhação de anagramas, você terá 5 chances para acertar!|")
print("---------------------------------------------------------------------------------------")
time.sleep(2)
clear_screen()
chances = 1

while(chances <= 5):
    palavra_printar = ''.join(palavra)
    print("Anagrama: {}".format(palavra_printar.lower()))
    chute = input("Escreva seu chute: ")
    if chute == palavra_escolhida_teste.lower():
        print("Você acertou!")
        print("Você precisou de {} chance(s)".format(chances))
        exit(0)
    elif(chances != 5):
        print("Você errou, tente novamente")
        chances += 1
        time.sleep(1)
        clear_screen()
    else:
        print("Suas chances acabaram!")
        print("A palavra era: {}".format(palavra_escolhida_teste))
        exit(0)
        