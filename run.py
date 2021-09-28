import random

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
