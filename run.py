import random
from hangman_pictures import hangman_image_state_easy
from hangman_pictures import hangman_image_state_medium
from hangman_pictures import hangman_image_state_hard
from time import sleep


def user_input():
    print("HANGMAN")
    print("\n")
    name = str(input("Input your name:\n")).upper()
    print("\n")
    print(f"Hi {name} are you ready to play hangman?")
    print('Choose from the 3 options....')
    print("DRAGON, CITIES or STANDARD")
    print("\n")
    game_choice(name)


def game_choice(name):
    while True:
        game_choice = input("Please choose your game: ").upper()
        print("\n")
        if game_choice == "DRAGON":
            with open("dragon_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                print(f"{name}, you chose the dragon words")
                get_game_level(picked, name)
                break
        elif game_choice == "CITIES":
            with open("cities_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                print(f"{name}, you chose the cities words")
                get_game_level(picked, name)
                break
        elif game_choice == "STANDARD":
            with open("words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                print(f"{name}, you chose the standard words")
                get_game_level(picked, name)
                break
        else:
            print(f"{name} that is not a valid choice, please try again")
            print("You must chose from, DRAGON, CITIES or STANDARD")
            print("\n")
            continue


def get_game_level(picked, name):
    """
    This function will take the users choice of difficulty for
    the game The choices are easy with 8 chances, medium
    with 6 chances, hard with 3 chances
    """
    while True:
        print('Chose from the 3 options....')
        print("EASY MEDIUM HARD")
        print("\n")
        game_level = input("Please choose your level:\n").upper()
        if game_level == "EASY":
            guesses_left = 8
            hangman_image_state(game_level, guesses_left)
            run_game_choice(
                hangman_image_state, guesses_left, game_level, picked, name)
        elif game_level == "MEDIUM":
            guesses_left = 6
            hangman_image_state(game_level, guesses_left)
            run_game_choice(
                hangman_image_state, guesses_left, game_level, picked, name)
        elif game_level == "HARD":
            guesses_left = 3
            hangman_image_state(game_level, guesses_left)
            run_game_choice(
                hangman_image_state, guesses_left, game_level, picked, name)


def hangman_image_state(game_level, guesses_left):
    if game_level == "EASY":
        hangman_image_state_easy(guesses_left)
    elif game_level == "MEDIUM":
        hangman_image_state_medium(guesses_left)
    elif game_level == "HARD":
        hangman_image_state_hard(guesses_left)


def think():
    for i in range(7):
        print(".")
        sleep(.5)
    print()


def update(word_as_a_list, secret_word):
    """
    This function updates the secret word with the correct
    guessed letter T-I-S-I-S-T-E-GUESS
    """

    for i in secret_word:
        secret_word = "".join(word_as_a_list)
        print(i, end = " ")


def run_game_choice(hangman_image_state, guesses_left, game_level, picked, name):
    """
    This function chooses which set of words to chose from
    """

    print("The word has", len(picked), "letters")
    print(f"{name}, you have {guesses_left} guesses")
    print("Let me think of a word")
    think()
    print(f"{name}, your chosen word is: ")
    print("\n")
    secret_word = list("-") * len(picked)
    word_as_a_list = list(picked)
    update(word_as_a_list, secret_word)
    print("\n")
    guessed_letters = []
    guessed = False
    while not guessed and guesses_left > 0:
        guess = input(f"{name}, please guess a letter:\n")[0].upper()
        print("Let me check")
        think()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"{name}, You already guessed that letter {guess}")
                print("Have another guess")
                print(guessed_letters)
                print(f"{name}, you have {guesses_left} guesses left")
                print("\n")
                update(word_as_a_list, secret_word)
                print("\n")
                hangman_image_state(game_level, guesses_left)
                print("\n")
                print("================================")
                print("\n")
            elif guess not in picked:
                print(f"{name}, {guess}, is not in the word.")
                guesses_left -= 1
                guessed_letters.append(guess)
                print(f"{name} letters guessed so far are {guessed_letters}")
                print(f"{name}, you have {guesses_left} guesses left")
                print("\n")
                update(word_as_a_list, secret_word)
                print("\n")
                hangman_image_state(game_level, guesses_left)
                print("\n")
                print("================================")
                print("\n")
                if guesses_left == 0:
                    print(f"{name} you lost! The secret word was {picked}")
                    print(f"{name}, you have {guesses_left} guesses left")
                    play_again = input("Do you want to play again? Y/N:\n").upper()
                    if play_again == "Y":
                        user_input()
                    else:
                        exit()
                    print("\n")
                    print("================================")
                    print("\n")
            elif guess in picked:
                print(f"Good job {name}, {guess}, is in the word!")
                guessed_letters.append(guess)
                print(f"{name} letters guessed so far are {guessed_letters}")
                index = 0
                for i in word_as_a_list:
                    if i == guess:
                        secret_word[index] = guess
                    index += 1
                print("\n")
                update(word_as_a_list, secret_word)
                print("\n")
                hangman_image_state(game_level, guesses_left)
                print("\n")
                print("================================")
                print("\n")
                if "-" not in secret_word:
                    guessed = True
                    print(f"Great job {name}, you guessed it!")
                    print(f"The secret word I chose was {picked}")
                    print("\n")
                    print("================================")
                    print("\n")
                    play_again = input("Do you want to play again? Y/N:\n").upper()
                    if play_again == "Y":
                        user_input()
                    else:
                        exit()


user_input()
