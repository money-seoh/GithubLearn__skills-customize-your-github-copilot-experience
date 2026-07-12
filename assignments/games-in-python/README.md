
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a text-based Hangman game in Python. In this assignment, you will practice loops, conditionals, and string handling while managing game state from start to finish.

## 📝 Tasks

### 🛠️	Set Up the Game State

#### Description
Create the initial game setup using the starter code. Choose a random word from the provided list and initialize all variables needed to run the game.

#### Requirements
Completed program should:

- Randomly select one secret word from the predefined list.
- Initialize a collection for guessed letters.
- Initialize counters for incorrect guesses and maximum allowed incorrect guesses.
- Display the starting game progress using underscores for unknown letters.


### 🛠️	Implement the Game Loop

#### Description
Build the main gameplay loop where the player enters letter guesses, the program validates and processes input, and the game ends with a final result.

#### Requirements
Completed program should:

- Prompt the user to enter one letter each turn.
- Reveal correctly guessed letters in their correct positions.
- Decrease remaining attempts for incorrect guesses.
- Continue until the player either guesses the full word or runs out of attempts.
- Print a clear win or lose message at the end of the game.
