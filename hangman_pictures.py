def hangman_image_state_easy(guesses_left):
    """
    This function shows the hangman image depending on
    how many guesses left the user has.
    """

    if guesses_left == 8:
        print('     ',  '      ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
    if guesses_left == 7:
        print('     ',  '------')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('     ',  '|     ')
        print('--------------')
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


def hangman_image_state_medium(guesses_left):
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


def hangman_image_state_hard(guesses_left):
    """
    This function shows the hangman image depending on
    how many guesses left the user has.
    """

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
