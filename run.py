import random


def user_input():
    print("HANGMAN")
    print("\n")
    name = str(input("Input your name: ")).upper()
    print("\n")
    print(f"Hi {name} are you ready to play hangman?")
    print('Choose from the 3 options....')
    print("DRAGON, CITIES or STANDARD")
    print("\n")


def get_random_word():
    """
    This function returns a random word to start the game
    """

    if game_choice == "DRAGON":
        with open("dragon_words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            picked = random.choice(words).upper()
            print(picked)
    elif game_choice == "CITIES":
        with open("cities_words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            picked = random.choice(words).upper()
            print(picked)
    elif game_choice == "STANDARD":
        with open("words.txt", "r") as file:
            allText = file.read()
            words = list(map(str, allText.split()))
            picked = random.choice(words).upper()
            print(picked)


def hangman_image_state(guesses_left):
    """
    This function shows the hangman image depending on
    how many guesses left the user has.
    """

    if guesses_left == 6:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 5:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 4:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|    |')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 3:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|   /|')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 2:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|   /|\\')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 1:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|   /|\\')
        print('     ',  '|   / ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 0:
        print('     ',  '------')
        print('     ',  '|    |')
        print('     ',  '|    O')
        print('     ',  '|   /|\\')
        print('     ',  '|   / \\')
        print('     ',  '|     ')
        print('--------------')


user_input()
