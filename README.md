# Ultimate Hangman

### Aim
The aim is to provide a fun and excitiong game where the user can escape the toils of day to day life for a few moments.

## Description
This game of Ultimate Hangman provides the user with three optional catagories to choose from. Depending on their choice the words will be related to that catagory. They are then given three further options to select the difficulty level they require, easy, where they will get 8 guesses, medium, where they will get 6 guesses and hard where they will only get 3 guesses. The selected catagory word is hidden behind - - - and the user is invited to have a guess at a letter. If they get it correct the hidden word will reveal where that letter fits into the word and they will be invited to have another go. If the user guesses incorrectly they will be informed of their choice and a list of letters they have already guessed. A picture of the hangman will be displayed along with the number of guesses they have remaining. Once the user has guessed the word or had failed to guess the word they will be informed of the result, the word they were trying to guess and receive an invitiation to play again or not.

The live game can be viewed [here](https://ultimate-hangman.herokuapp.com/).

## Wireframes
[Click here for the desktop wireframe](assets/images/hangman.png)

## Client Stories

1. As an new visitor to the website, I want to easily be able to understand what the game is about.
2. As an new visitor to the website, I want to easily be able to understand how the game works.
3. As a visitor to the website, I want to have a choice of game catagories.
4. As a visitor to the website, I want to have a choice of difficulty levels.
5. As a user I want to know if I guessed correctly and see it displayed in the hidden word.
6. As a user I want to know if I guessed incorrectly and see a hangman image and how many guesses I have left.
7. As a user I want to know if I have already guessed a letter.
8. As a user I want to know if I have won or lost.
9. As a user I want to have the choice to play again or not.

## Features

* User input to collect the name of the user to use in throughout the game.
* User has choice to pick from three categoris of words fot the game.
* User has choice of three difficulty levels for their game.
* The chosen word for the game is displayed as a hidden word.
* The hangman image is displayed along with how many guesses the user has remaining.
* Result of guess is displayed to the user.
* Result of the game is displayed to the user.
* An option to play again is displayed to the user.

## Bugs
### Fixed
* I found a bug with the user guess when playing. If the user didn't enter anything or the user input more than one letter the program would just ask for the user to input a letter again. So I added print statements to respont to the user. Also if the user input a number the program would jump back to the difficulty level choices. To solve this I used a while loop and if elif statement.

### Unfixed
* None

## Testing
This project has been tested throughout its inception. Each input has been thoroughly tested to make sure that any invalid inputs are handled correctly and a response is shown to the user.

* Name input - 

* Game catagory input - This has been tested so that it will only accept the corect three words. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again.

* Game level input - This has been tested so that it will only accept the corect three words, EASY, MEDIUM and HARD. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again.

* Guess input - This has been tested so that it will only accept the corect letters. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again. For example if the user has already guessed that letter, a response to the user will read, "You have already guessed that letter" and ask them to try again whilst also showing them a list of the letters they have guessed. If the guess is not in the word, the user will get a response telling them so and a life will be lost. If the guess is in the word they will get a response congratulating them and updating the hidden word.

* Play again input - This has been tested so that it will only accept the corect letters. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. It checkes for the "Y" and if so it will start the game again, if anythong else is pressed the game will end and a response will be returned to the user to say Goodbye.

### Validator Testing