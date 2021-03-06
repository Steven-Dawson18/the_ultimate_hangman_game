# Ultimate Hangman

### Aim
The aim is to provide a fun and exciting game where the user can escape the toils of day to day life for a few moments.

## Description
This game of Ultimate Hangman provides the user with three optional catagories to choose from. Depending on their choice the words will be related to that catagory. They are then given three further options to select the difficulty level they require, easy, where they will get 8 guesses, medium, where they will get 6 guesses and hard where they will only get 3 guesses. The selected catagory word is hidden behind - - - and the user is invited to have a guess at a letter. If they get it correct the hidden word will reveal where that letter fits into the word and they will be invited to have another go. If the user guesses incorrectly they will be informed of their choice and a list of letters they have already guessed. A picture of the hangman will be displayed along with the number of guesses they have remaining. Once the user has guessed the word or had failed to guess the word they will be informed of the result, the word they were trying to guess and receive an invitiation to play again or not.

The live game can be viewed [here](https://ultimate-hangman.herokuapp.com/).

![Ultimate Hangman](assets/images/responsiveness.png)

## How to play

To play Ultimat Hangman you will first need to enter your name. You will then be given three choices of game category. Enter the category choice adn you will then be given three choices of difficulty level to play. Easy gives you 8 guesses, medium gives you 6 guesses and hard gives you 3 guesses.
Once you have chosen the game and level you will have the secret word displayed behind dashe. It will tell you how many letters there are in the word and how many guesses you have. You will then be asked to make a guess of a letter. Once you enter a guess the computer wil check if your guess is in the secret word. If it is the the letter will be displayed amongst the dashes in the position it holds in the word. If you guess incorrectly you will see the hangman picture and be told that the letter is not in the secret word, with how many guesses you have remaining. If you manage to guess the word within the number of guesses for your chosen level you will be congratulated and asked if you want to play again or not. If you fail to guess the word, you will be told that you failed to guess correctly and the secret word you were trying to guess will be displayed. You will then be asked if you wish to play again or not.

## Wireframes
[Click here for the wireframe](assets/images/hangman.png)

## Client Stories

1. As an new visitor to the website, I want to easily be able to understand what the game is about.
2. As a visitor to the website, I want to have a choice of game catagories.
3. As a visitor to the website, I want to have a choice of difficulty levels.
4. As a user I want to know if I guessed correctly and see it displayed in the hidden word.
5. As a user I want to know if I guessed incorrectly and see a hangman image and how many guesses I have left.
6. As a user I want to know if I have already guessed a letter.
7. As a user I want to know if I have won or lost.
8. As a user I want to have the choice to play again or not.


## Flow

![Game flow](assets/images/flowchart_hangman.jpg)

## Features

* User input to collect the name of the user to use in throughout the game.

[User input](assets/images/client_story_1.png)

* User has choice to pick from three categories of words for the game.

[Game Category](assets/images/client_story_2.png)

* User has choice of three difficulty levels for their game.

[Game Levels](assets/images/client_story_3.png)

* The chosen word for the game is displayed as a hidden word.

[Guess confirmation](assets/images/client_story_4.png)

* The hangman image is displayed along with how many guesses the user has remaining.

[Guess incorrect](assets/images/client_story_5.png)

* Result of guess is displayed to the user.
* Result of the game is displayed to the user.
* An option to play again is displayed to the user.

[Lost](assets/images/client_story_75.png)

### Future Features

* A further feature to improve this game could be to add a hint for the secret word. Possibly by using an API.

* There could possibly be a competition mode where the user tries to guess a word in as few goes as possible and the result gets placed on a high score board.

## Technologies Used

* Python

### Libraries Used

* Random
The random library was used to select a random word from the txt files.

* Time - sleep
The time library was utilised in order to use the sleep method. This method when implemented in the game and creates the impression that the computer is checking/thinking which adds to the suspense and experience of the game.

## Bugs
### Fixed
* On the user name input I found that the user could simply enter what they wanted or indeed nothing at all. To fix this I used a while loop to check the input was alpha.
* I found a bug with the user guess when playing. If the user didn't enter anything or the user input more than one letter the program would just ask for the user to input a letter again. So I added print statements to respont to the user. 
* Also if the user input a number the program would jump back to the difficulty level choices. To solve this I used a while loop and if elif statement.
* To stop an error occuring where the user could enter more than one character as the guess, I had it select only the first character that was input. However this proved troublesome as if I entered numbers or special characters it through an error. To solve this I added elif else statements to the chame_choice function to validate the input.
* There were numerous faults in the terminal relating to lines that were too long. I solved these by rewording print statements and moving function parameters on to a different line.
* I noticed that the number of letters in the word was being printed before the computer thinks of the word, so I adjusted the order of statements.

### Known issues
* I am aware that there is an issue in the program when the think function is running, but I have been unable to come up with a solution to this. The user can input another letter whilst the program is checking if the previous letter is in the word. Any letters the user inputs still get processed and it does not throw up a fault in the game. It's just not as aesthetically pleasing as I would have liked.

## Data Model

I decided to use text files for the words each game will run to get a secret word. I placed these in a dictionary and called the key to access the text file that is needed to run each game.

## Testing

The website was extensively tested as it was developed using:
* console.log().
* The terminal by printing the expected outcome.
* Testing scenarios manually.

This project has been tested throughout its inception. Each input has been thoroughly tested to make sure that any invalid inputs are handled correctly and a response is shown to the user.

* Name input - This has been tested so that it will only accept letters. I did this by creating a while loop to check if the input is alpha(). To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method.

* Game catagory input - This has been tested so that it will only accept the corect three words. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again.

* Game level input - This has been tested so that it will only accept the corect three words, EASY, MEDIUM and HARD. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again.

* Guess input - This has been tested so that it will only accept the letters. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. I have also checked for any other invalid inputs and returned a message to the user to state the error and to input again. For example if the user has already guessed that letter, a response to the user will read, "You have already guessed that letter" and ask them to try again whilst also showing them a list of the letters they have guessed. If the guess is not in the word, the user will get a response telling them so and a life will be lost. If the guess is in the word they will get a response congratulating them and updating the hidden word.

* Play again input - This has been tested so that it will only accept the corect letters. To make sure that the input is correct I have made sure that any input is converted to capitals using the upper() method. It checkes for the "Y" and if so it will start the game again, if anythong else is pressed the game will end and a response will be returned to the user to say Goodbye.

### Testing Client Stories

1. As an new visitor to the website, I want to easily be able to understand what the game is about.

![Game information](assets/images/client_story_1.png)

* The game immediately informs you that you are about to play hangman. Once you enter your name you are then told how to play the game, as shown in the image above.

2. As a visitor to the website, I want to have a choice of game catagories.

![Game Category](assets/images/client_story_2.png)

* The user is given three choices of category, Dragons, Cities and Standard words.

3. As a visitor to the website, I want to have a choice of difficulty levels.

![Game Levels](assets/images/client_story_3.png)

* The user is given three levels of difficulty to choose from.

4. As a user I want to know if I guessed correctly and see it displayed in the hidden word.

![Guess confirmation](assets/images/client_story_4.png)

* The user is congratulated on getting a guess correct and the letter guessed is input into the hidden word and displayed to the user.

5. As a user I want to know if I guessed incorrectly and see a hangman image and how many guesses I have left.

![Guess incorrect](assets/images/client_story_5.png)

* The user is informed if their guess is incorrect. A list of the letters they have guessed so far will be displayed along with the number of guesses they have left and an image of the hangman position they are at.

6. As a user I want to know if I have already guessed a letter.

![Guessed already](assets/images/client_story_6.png)

* The user will be informed if they have already guessed a letter and asked to try again. They will not lose a life.

7. As a user I want to know if I have won or lost.

![Win](assets/images/client_story_7.png)
![Lost](assets/images/client_story_75.png)

* The user is informed if they won or lost the game with a statement being returned to them. They are also informed of what the hidden word was.

8. As a user I want to have the choice to play again or not.

![Play again](assets/images/client_story_8.png)

* When the user has either been successfull in guessing the word or failed to guess the word they will be invited to play again. If they select yes they will be invited to enter their name again to restart. If they choose no then they will be shown a goodbye message and the game will end.

### Validator Testing

* Each Python file was run through pep8 online and returned no errors.

![Click here for the PEP8 online Validation of run.py](assets/images/pep8_validation.png)

![Click here for the PEP8 online Validation of hangman_pictures.py](assets/images/pep8_online_validation_2.png)

### Testing on Devices

* I have tested the deployed Heroku app on different devices such as Macbook Pro, Samsung Galaxy Tab and iphone. I have found no issues with the game working on them.

## Deployment on Heroku

* Fork or clone this repository
* Log onto Heroku and click the create new app button
* Enter a unique name for your application
* Select the region closest to you
* Set environment in Heroku App
* Go to settings, then click on reveal config vars
* Enter your key value pairs - KEY = PORT, VALUE = 8000
* Add buildpack python
* Add buildpack nodejs
* Set your deployment method to 'GitHub'
* Search for the repository you wish to deploy from
* Enable automatic deploy

## Credits
* Code Institute for the deployment terminal

### Code
* The run_game_choice function was adapted from this tutorial https://www.youtube.com/watch?v=m4nEnsavl6w&t=173s

* The think function was adapted from this tutorial https://www.youtube.com/watch?v=7sVnul-StrU&t=992s

* The update function was adapted from this tutorial https://www.youtube.com/watch?v=7sVnul-StrU&t=992s

### Content
None

### Media
None

### Acknowledgments
My mentor Can Sucullu for his advice and guidance.