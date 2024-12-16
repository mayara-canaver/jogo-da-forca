import sys
import random

import requests
from bs4 import BeautifulSoup

import hangman_texts

def get_word_online():
    try:
        html_file = requests.get("https://www.palabrasaleatorias.com/").text
        soup = BeautifulSoup(html_file, 'lxml')

        word = soup.find(attrs={'style':'font-size:3em; color:#6200C5;'}).text
        word = word.strip

        return word
    
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving word online: {e}")

        return random.choice(hangman_texts.animals_storage)

def win(i, secret_word, right_letter):
    if i < 5 and len(right_letter) == len(set(secret_word)):
        print("You win!")

        return 1
    
    if i == 5:
        print(str(hangman_texts.phases[5]))
        print("Game over.")
        print("The secret word was:", secret_word)

        return 2
    
    return 0

def insert_letter():
    letter = input("Guess a letter:\n\n")

    if letter.isdigit():
        print(random.choice(hangman_texts.error_message))

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
    print("\n\n----------- Topics -----------\n")
    print("1 - Animals")
    print("2 - Foods")
    print("3 - Objects")
    print("4 - Hard level (online only)\n")

    while True:
        choice = input("Choose a topic:")

        if choice == '1':
            return random.choice(hangman_texts.animals_storage)
        
        elif choice == '2':
            return random.choice(hangman_texts.foods_storage)
        
        elif choice == '3':
            return random.choice(hangman_texts.objects_storage)
        
        elif choice == '4':
            return get_word_online()
        
        else:
            print(random.choice(hangman_texts.error_message))

def play_again():
    print("Another round? Let's go!\n")
    print("1 - Yes")
    print("2 - No\n")

    while True:
        choice = input("Your choice:\n")

        if choice == '1':
            return phase()
        
        elif choice == '2':
            sys.exit()

        else:
            print("Invalid input. Please try again.")

def phase():
    right_letter, wrong_letter = [], []

    i = 0

    secret_word = choose_database()

    while win(i, secret_word, right_letter) == 0:
        print(str(hangman_texts.phases[i]))

        letters_to_guess(secret_word, right_letter)

        letter = insert_letter()

        if verify_letter(letter, secret_word, right_letter, wrong_letter):
            print("Correct answer!")

        else:
            i += 1
            print("Wrong answer. Try again.")

    play_again()
