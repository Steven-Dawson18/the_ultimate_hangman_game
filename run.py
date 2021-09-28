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
    get_random_word()


def get_random_word():
    """
    This function returns a random word to start the game
    """
    while True:
        game_choice = input("Please choose your game: ").upper()
        print("\n")
        if game_choice == "DRAGON":
            with open("dragon_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                run_game_choice(hangman_image_state, guesses_left, picked, name)
        elif game_choice == "CITIES":
            with open("cities_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                run_game_choice(hangman_image_state, guesses_left, picked, name)
        elif game_choice == "STANDARD":
            with open("words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                run_game_choice(hangman_image_state, guesses_left, picked, name)


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


def update(word_as_a_list, secret_word):
    """
    This function updates the secret word with the correct
    guessed letter T-I-S-I-S-T-E-GUESS
    """

    for i in secret_word:
        secret_word = "".join(word_as_a_list)
        print(i, end = " ")

def run_game_choice(hangman_image_state, guesses_left, picked, name):
    """
    This function choses which set of words to chose from
    """

    print(f"{name} game started")
    print(picked)
    print("The word has", len(picked), "letters")
    print(f"{name}, your chosen word is: ")
    print("\n")
    secret_word = list("-") * len(picked)
    word_as_a_list = list(picked)
    print("\n")
    guessed_letters = []
    guessed = False


user_input()
