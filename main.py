import time
import random

word_bank = ["linux", "adam", "python", "easy", "couch", "wordle", "beer", "flower", "chair"]
word = random.choice(word_bank)
display_word = word
guess = ""
display = "_" * len(word)
count = 0
number_of_guesses = len(word) - 1
victory = False
hangman = ["""   # https://www.fssnip.net/mO/title/Hangman  - drawing taken from this link
____
|/   |
|   
|    
|    
|    
|
|_____
""",
           """
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____
""",
           """
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____
""",
           """
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____
""",
           """
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____
""",
           """
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \
|
|_____
""",
           """
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____
"""]


def validateInput(choice, min, max):
    if choice in range(min, max):
        return True
    else:
        return False


def mainMenu():
    global number_of_guesses
    print("Hangman Game")
    print("1: Start game")
    option = int(input("---->"))
    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        print(hangman[0])
        play()

        time.sleep(5)
    if option > 24:
        print("Please enter a valid option")
        mainMenu()


def play():
    global count
    global number_of_guesses
    global guess
    global word
    global display
    global victory

    guess = input("----->")
    guess = guess.strip()
    if guess in word:
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
        if word == '_' * len(word):
            print("Well done you guessed correctly!!!")
            victory = True
        if not victory:
            play()

    elif guess not in word:
        count += 1
        if count == 0:
            print(hangman[count])
            print(display)
            print("You have " + str(number_of_guesses) + " attempts")
        if count == len(word) - 1:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print(hangman[6])
            print("You have " + str(number_of_guesses) + " attempts left you lose")
            print("The word was " + display_word)
        if number_of_guesses <= 0:
            exit()
        if count == 1:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()
        if count == 2:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()
        if count == 3:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()
        if count == 4:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()
        if count == 5:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()
        if count == 6:
            print(hangman[count])
            number_of_guesses = number_of_guesses - 1
            print("You have " + str(number_of_guesses) + " attempts")
            gameLoop()


def gameLoop():
    play()


# TODO
def wordGuess():
    word_guess = input("Please guess the full word : ")
    if word_guess == word:
        print("You WIN!")


mainMenu()
if __name__ == '__main__':
    print()
