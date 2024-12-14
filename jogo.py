import sys

import requests
from bs4 import BeautifulSoup

import random
import textos

def palavra_online():
    html_file = requests.get("https://www.palabrasaleatorias.com/").text
    soup = BeautifulSoup(html_file, 'lxml')
    word = soup.find(attrs={'style':'font-size:3em; color:#6200C5;'}).text
    return word

def ganhou(i, palavra, letra_certa):
    if i < 5 and len(letra_certa) == len(set(palavra)):
        print("Você ganhou!")
        return 1
    if i == 5:
        print(str(textos.fases[5]))
        print("Você perdeu.")
        print("A palavra era:", palavra)
        return 2
    return 0

def insere_letra():
    letra = input("Digite uma letra\n\n")
    if letra.isdigit():
        print(random.choice(textos.mensagem_erro))
        return insere_letra()
    return letra

def verifica_letra(letra, palavra, letra_certa, letra_errada):
    if letra in palavra and letra not in letra_certa:
        letra_certa.append(letra)
        return True
    if letra not in palavra and letra not in letra_errada:
        letra_errada.append(letra)
        return False

def letras_restante(palavra, letra_certa):
    esp = ""
    for letras in palavra:
        if letras not in letra_certa:
            esp = "_ "
        elif letras in letra_certa:
            esp = letras
        print(esp, end="")
    print("")

def escolher_banco():
    print("\n\n----------- Temas -----------\n")
    print("1 - Animais")
    print("2 - Alimentos")
    print("3 - Objetos")
    print("4 - Nível Hard (Apenas Online)\n")
    escolha = int(input("Escolha um tema:"))

    if escolha == 1:
        return random.choice(textos.banco_animais)
    if escolha == 2:
        return random.choice(textos.banco_alimentos)
    if escolha == 3:
        return random.choice(textos.banco_objetos)
    if escolha == 4:
        return True
    print(random.choice(textos.mensagem_erro))
    return escolher_banco()

def final():
    print("Deseja jogar novamente?\n")
    print("1 - Sim")
    print("2 - Não\n")
    res_final = int(input("Sua escolha:\n"))

    if res_final == 1:
        return fase()
    if res_final == 2:
        sys.exit()
    print(random.choice(textos.mensagem_erro))
    return final()

def fase():
    letra_certa = []
    letra_errada = []
    i = 0
    palavra = escolher_banco()
    if palavra:
        palavra = palavra_online()
    while ganhou(i, palavra, letra_certa) == 0:
        print(str(textos.fases[i]))
        letras_restante(palavra, letra_certa)
        letra = insere_letra()
        if verifica_letra(letra, palavra, letra_certa, letra_errada):
            print("Letra correta!")
        else:
            i += 1
            print("Letra errada, tente novamente.")
    final()
