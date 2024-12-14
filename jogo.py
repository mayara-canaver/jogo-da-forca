import sys
import random

import requests
from bs4 import BeautifulSoup

import textos

def palavra_online():
    html_file = requests.get("https://www.palabrasaleatorias.com/").text
    soup = BeautifulSoup(html_file, 'lxml')
    word = soup.find(attrs={'style':'font-size:3em; color:#6200C5;'}).text

    return word

def ganhou(i, secret_word, right_letter):
    if i < 5 and len(right_letter) == len(set(secret_word)):
        print("Você ganhou!")

        return 1
    
    if i == 5:
        print(str(textos.fases[5]))
        print("Você perdeu.")
        print("A palavra era:", secret_word)

        return 2
    
    return 0

def insere_letra():
    letra = input("Digite uma letra\n\n")

    if letra.isdigit():
        print(random.choice(textos.mensagem_erro))

        return insere_letra()
    
    return letra

def verifica_letra(letra, secret_word, right_letter, wrong_letter):
    if letra in secret_word and letra not in right_letter:
        right_letter.append(letra)

        return True
    
    if letra not in secret_word and letra not in wrong_letter:
        wrong_letter.append(letra)

        return False

def letras_restante(secret_word, right_letter):
    esp = ""

    for letras in secret_word:
        if letras not in right_letter:
            esp = "_ "

        elif letras in right_letter:
            esp = letras

        print(esp, end="")

    print("")

def escolher_banco():
    print("\n\n----------- Temas -----------\n")
    print("1 - Animais")
    print("2 - Alimentos")
    print("3 - Objetos")
    print("4 - Nível Hard (Apenas Online)\n")
    choice = int(input("Escolha um tema:"))

    if choice == 1:
        return random.choice(textos.banco_animais)
    if choice == 2:
        return random.choice(textos.banco_alimentos)
    if choice == 3:
        return random.choice(textos.banco_objetos)
    if choice == 4:
        return True
    print(random.choice(textos.mensagem_erro))
    return escolher_banco()

def final():
    print("Deseja jogar novamente?\n")
    print("1 - Sim")
    print("2 - Não\n")
    choice = int(input("Sua escolha:\n"))

    if choice == 1:
        return fase()
    
    if choice == 2:
        sys.exit()
        
    print(random.choice(textos.mensagem_erro))
    return final()

def fase():
    right_letter = []
    wrong_letter = []

    i = 0

    secret_word = escolher_banco()

    if secret_word:
        secret_word = palavra_online()
    while ganhou(i, secret_word, right_letter) == 0:
        print(str(textos.fases[i]))
        letras_restante(secret_word, right_letter)
        letra = insere_letra()
        if verifica_letra(letra, secret_word, right_letter, wrong_letter):
            print("Letra correta!")
        else:
            i += 1
            print("Letra errada, tente novamente.")
    final()
