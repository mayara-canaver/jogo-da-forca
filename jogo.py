import sys
import random

import requests
from bs4 import BeautifulSoup

import textos

def get_word_online():
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

def insert_letter():
    letter = input("Digite uma letra\n\n")

    if letter.isdigit():
        print(random.choice(textos.mensagem_erro))

        return insert_letter()
    
    return letter

def verify_letter(letter, secret_word, right_letter, wrong_letter):
    if letter in secret_word and letter not in right_letter:
        right_letter.append(letter)

        return True
    
    if letter not in secret_word and letter not in wrong_letter:
        wrong_letter.append(letter)

        return False

def letters_to_guess(secret_word, right_letter):
    blank_space = ""

    for letters in secret_word:
        if letters not in right_letter:
            blank_space = "_ "

        elif letters in right_letter:
            blank_space = letters

        print(blank_space, end="")

    print("")

def choose_database():
    print("\n\n----------- Temas -----------\n")
    print("1 - Animais")
    print("2 - Alimentos")
    print("3 - Objetos")
    print("4 - Nível Hard (Apenas Online)\n")

    while True:
        choice = input("Escolha um tema:")

        if choice == '1':
            return random.choice(textos.banco_animais)
        
        elif choice == '2':
            return random.choice(textos.banco_alimentos)
        
        elif choice == '3':
            return random.choice(textos.banco_objetos)
        
        elif choice == '4':
            return get_word_online()
        
        else:
            print(random.choice(textos.mensagem_erro))

def play_again():
    print("Another round? Let's go!\n")
    print("1 - Yes")
    print("2 - No\n")

    while True:
        choice = input("Your choice:\n")

        if choice == '1':
            return fase()
        
        elif choice == '2':
            sys.exit()

        else:
            print("Invalid input. Please try again.")

def fase():
    right_letter, wrong_letter = [], []

    i = 0

    secret_word = choose_database()

    while ganhou(i, secret_word, right_letter) == 0:
        print(str(textos.fases[i]))

        letters_to_guess(secret_word, right_letter)

        letter = insert_letter()

        if verify_letter(letter, secret_word, right_letter, wrong_letter):
            print("Letra correta!")

        else:
            i += 1
            print("Letra errada, tente novamente.")

    play_again()
