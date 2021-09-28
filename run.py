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
    game_choice(name)


def get_random_word(name):
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
                return picked
                run_game_choice(game_choice, hangman_image_state, picked, name)
        elif game_choice == "CITIES":
            with open("cities_words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                return picked
                run_game_choice(game_choice, hangman_image_state, picked, name)
        elif game_choice == "STANDARD":
            with open("words.txt", "r") as file:
                allText = file.read()
                words = list(map(str, allText.split()))
                picked = random.choice(words).upper()
                return picked
                run_game_choice(game_choice, hangman_image_state, picked, name)


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


def run_game_choice(game_choice, hangman_image_state, picked, name):
    """
    This function choses which set of words to chose from
    """
    if game_choice == 'DRAGON':
        print(f"{name}, you chose the medium words")
        picked = get_random_word(name)
        print("The word has", len(picked), "letters")
        print(f"{name}, your chosen word is: ")
        print("\n")
        secret_word = list("-") * len(picked)
        word_as_a_list = list(picked)
        update(word_as_a_list, secret_word)
        print("\n")
        guessed_letters = []
        guessed = False
        guesses_left = 6
        while not guessed and guesses_left > 0:
            guess = input(f"{name}, please guess a letter: ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print(f"{name}, You already guessed that letter {guess}")
                    print("Have another guess")
                    print(guessed_letters)
                    print("\n")
                    update(word_as_a_list, secret_word)
                    print("\n")
                    hangman_image_state(guesses_left)
                    print("\n")
                    print("================================")
                    print("\n")
                elif guess not in picked:
                    print(f"{name}, {guess}, is not in the word.")
                    guesses_left -= 1
                    guessed_letters.append(guess)
                    print(f"{name} the letters you have guessed so far are {guessed_letters}")
                    print(f"{name}, you have {guesses_left} guesses left")
                    print("\n")
                    update(word_as_a_list, secret_word)
                    print("\n")
                    hangman_image_state(guesses_left)
                    print("\n")
                    print("================================")
                    print("\n")
                    if guesses_left == 0:
                        print(f"Unlucky {name} you lost! the secret word was {picked}")
                        play_again = input("Do you want to play again? Y/N: ").upper()
                        if play_again == "y":
                            run_game_choice()
                        else:
                            exit()
                        print("\n")
                        print("================================")
                        print("\n")
                elif guess in picked:
                    print(f"Good job {name}, {guess}, is in the word!")
                    guessed_letters.append(guess)
                    print(f"{name} the letters you have guessed so far are {guessed_letters}")
                    index = 0
                    for i in word_as_a_list:
                        if i == guess:
                            secret_word[index] = guess
                        index += 1
                    print("\n")
                    update(word_as_a_list, secret_word)
                    print("\n")
                    hangman_image_state(guesses_left)
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
                        play_again = input("Do you want to play again? Y/N: ").upper()
                        if play_again == "y":
                            get_game_choice()
                        else:
                            exit()

user_input()
