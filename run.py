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

user_input()
