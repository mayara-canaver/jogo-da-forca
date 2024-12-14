import sys
import random

import hangman_texts
import hangman_functions

def how_to_play():
    print("Welcome to Hangman!")
    print("Guess the secret word one letter at a time.")
    print("You'll be given hints like the number of letters and a category.")
    print("For each incorrect guess, a part of the hangman is drawn.")
    print("Be careful, you have only 6 incorrect guesses before you lose!")

    return menu()

def menu():
    print("\n\n----------------- Welcome to Hangman Game! -----------------\n")
    print("1 - Start Game")
    print("2 - How to Play")
    print("3 - Exit\n")

    while True:
        choice = input("Make your selection:")

        if choice == '1':
            hangman_functions.fase()

        elif choice == '2':
            how_to_play()

        elif choice == '3':
            sys.exit()

        else:
            print(random.choice(hangman_texts.mensagem_erro))
            return menu()

menu()
