# Bagels, by Sergio 'Wolfnom' A. Knapik
# A deduction game, coded in 2022

import random

cheat_mode = False


def language_selection():
    invalid_input = True
    global cheat_mode

    while invalid_input:
        print("Hello! Please choose the game's language:\nOlá! Por favor escolha o idioma:")
        print("(type the language's number and press enter)\n(digite o número do idioma e pressione enter)\n\n")
        print("1. Português Brasileiro")
        lang = input(f"2. English\n")

        if lang == "1" or lang == "2":
            return int(lang)
        elif lang == "3":
            print("Cheat mode on")
            cheat_mode = True
        else:
            print("Invalid input! Please try again.\nValor inválido! Por favor, tente novamente.\n")


def game_start(language_selected):
    if language_selected == 1:
        game_br()
    elif language_selected == 2:
        game_en()


def guess_check(guess, number):
    # print("checking guess...")
    result = str()
    str_guess = str(guess)
    str_number = str(number)
    for i in range(0, 3):
        if str_guess[i] == str_number[i]:
            result += "Fermi "
        elif str_guess[i] in str_number:
            result += "Pico "
    if result == "":
        result = "Bagel"
    return result


def get_guess(guesses, lang, number):
    try:
        player_guess = int(input(f"Palpite {guesses}: "))
    except ValueError:
        if lang == "br":
            print("Entrada inválida. Deve ser um número!")
            return False
        if lang == "en":
            print("Invalid input. Must be a number!")
            return False
    else:
        if len(str(player_guess)) == 3:
            # print(player_guess)
            if player_guess == number:
                return True
            else:
                return guess_check(player_guess, number)
        else:
            if lang == "br":
                print("Ei, esse número não tem três dígitos!")
                return False
            if lang == "en":
                print("Hey, this number does not have three digits!")
                return False


def game_br():
    # print("Jogo em br")
    guesses = 0
    random_number = random.randint(100, 1000)
    game_end = False

    if cheat_mode:
        print(f"Psiu! A resposta certa é {random_number}")

    print("Estou pensando em um número de três dígitos.\nTente adivinhar que número é!\n"
          "Você tem dez palpites.\n\nDicas:\nSe eu falar 'Pico', você acertou um dígito mas na"
          " posição errada.\nSe eu falar 'Fermi', você acertou um dígito na posição certa.\n"
          "Mas se eu falar 'Bagels', nenhum dígito está certo.")

    while not game_end:
        guesses += 1

        player_guess = get_guess(guesses, "br", random_number)
        if player_guess == False:
            guesses -= 1
        elif player_guess == True:
            print("Parabéns! Você acertou!")
            game_end = True
        else:
            print(player_guess)

        if guesses > 9:
            print("Poxa! Acabaram os palpites!\nVocê perdeu.")
            game_end = True


def game_en():
    # print("Game in en")
    guesses = 0
    random_number = random.randint(100, 1000)
    game_end = False

    if cheat_mode:
        print(f"Psst! Right answer is {random_number}")

    print("I am thinking of a three digit number.\nTry to guess which number it is!\n"
          "You have ten chances.\n\nClues:\nIf I say 'Pico', you got one digit but in the"
          " wrong position.\nIf I say 'Fermi', you got one digit in the right position.\n"
          "But if I say 'Bagels', all digits are wrong.")

    while not game_end:
        guesses += 1

        player_guess = get_guess(guesses, "en", random_number)
        if player_guess == False:
            guesses -= 1
        elif player_guess == True:
            print("Great! You got it!")
            game_end = True
        else:
            print(player_guess)

        if guesses > 9:
            print("Oh no! There are no more guesses!\nYou lost.")
            game_end = True


game_start(language_selection())
