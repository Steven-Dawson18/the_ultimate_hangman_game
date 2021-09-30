import random
from hangman_pictures import hangman_image_state_easy
from hangman_pictures import hangman_image_state_medium
from hangman_pictures import hangman_image_state_hard
from time import sleep


def user_input():
    """
    This function introduces the game and takes a user input
    for their name which will be refferenced throughout the
    game.
    """
    print("*******************")
    print("HANGMAN")
    print("*******************")
    print("\n")
    print("This is a game where you have to guess a hidden word.")
    print("\n")
    print("There are three catagories and levels to choose from.")
    print("\n")
    print("To start please....")
    print("\n")
    while True:
        # Collects users name
        name = str(input("Enter your name:\n")).upper()
        if not name.isalpha():
            print("You. ust enter a character for your name")
            continue
        else:
            print("\n")
            print(f"Hi {name}, are you ready to play hangman?")
            print("There are three catagories to choose from")
            print("How to train your dragon")
            print("Worlds major Cities")
            print("Standard hangman catagory")
            print('Choose from the 3 options....')
            print("Enter either: DRAGON, CITIES or STANDARD")
            print("\n")
            game_choice(name)


def game_choice(name):
    """
    This function will take the input from the user and select
    a random word from the appropriate word.txt file.
    """
    while True:
        game_choice = input("Please choose your game: ").upper()
        print("\n")
        if game_choice == "DRAGON":
            with open("dragon_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                # print(picked)
                print(f"{name}, you chose the easy words")
                # run_game_choice(picked, name)
                get_game_level(picked, name)
                break
        elif game_choice == "CITIES":
            with open("cities_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                print(f"{name}, you chose the medium words")
                # run_game_choice(picked, name)
                get_game_level(picked, name)
                break
        elif game_choice == "STANDARD":
            with open("words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                print(f"{name}, you chose the hard words")
                get_game_level(picked, name)
                break
        else:
            print(f"{name} that is not a valid choice, please try again")
            print("You must chose from, EASY, MEDIUM, HARD")
            print("\n")
            continue


def get_game_level(picked, name):
    """
    This function will take the users choice of difficulty for
    the game. The choices are easy with 8 chances, medium
    with 6 chances and hard with 3 chances.
    """
    while True:
        print('Choose from the 3 difficulty options....')
        print("EASY MEDIUM HARD")
        print("\n")
        # Collects difficulty option from the user
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
    """
    This function changes the hangman image depending
    on the level chosen by the user.
    """
    if game_level == "EASY":
        hangman_image_state_easy(guesses_left)
    elif game_level == "MEDIUM":
        hangman_image_state_medium(guesses_left)
    elif game_level == "HARD":
        hangman_image_state_hard(guesses_left)


def think():
    """
    This function makes the game wait which makes it
    appear that the computer is thinking.
    """
    for i in range(5):
        i = "."
        print(i, end=" ")
        sleep(.3)


def update(word_as_a_list, secret_word):
    """
    This function updates the secret word with the correct
    guessed letter T-I-S-I-S-T-E-GUESS
    """

    for i in secret_word:
        secret_word = "".join(word_as_a_list)
        print(i, end=" ")


def run_game_choice(
        hangman_image_state, guesses_left, game_level, picked, name):
    """
    This function chooses which set of words to choose from
    """

    print("The word has", len(picked), "letters")
    print(f"{name}, you have {guesses_left} guesses")
    print("Let me think of a word")
    think()
    print("\n")
    print(f"{name}, your chosen word is: ")
    print("\n")
    secret_word = list("-") * len(picked)
    word_as_a_list = list(picked)
    update(word_as_a_list, secret_word)
    print("\n")
    guessed_letters = []
    guessed = False
    while not guessed and guesses_left > 0:
        guess = input(f"{name}, please guess a letter:\n").upper()
        print("Let me check")
        think()
        print("\n")
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
                    play_again = input(f"{name} play again? Y/N:\n").upper()
                    if play_again == "Y":
                        user_input()
                    else:
                        print(f"Thanks for playing {name}. Play again soon.")
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
                    play_again = input(f"{name} play again? Y/N:\n").upper()
                    if play_again == "Y":
                        user_input()
                    else:
                        print(f"Thanks for playing {name}. Play again soon.")
                        exit()
        elif len(guess) == 0:
            print(f"{name} that is not a valid input, try again")
            continue
        elif len(guess) > 1 and guess.isalpha():
            print(f"{name} that is not a valid input, try again")
            continue
        else:
            print(f"{name} you must provide a letter, try again")
            continue


user_input()
