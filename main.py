import random

word_bank = ["linux", "adam", "python", "easy", "couch", "wordle", "beer", "flower", "chair"]

word = random.choice(word_bank)
lives = len(word) - 1
hangman = ["""

# https://www.fssnip.net/mO/title/Hangman  - drawing taken from this link
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
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
|    
|    
|    
|
|_____
""", """  
____
|/   |
|   
|    
|    
|    
|
|_____
"""
           ]

hangman_status = lives
current = "_" * len(word)
x = list(current)
print(x)

guessed = []


def find_all(word, guess):
    return [i for i, letter in enumerate(word) if letter == guess]


def wordGuess():
    global word
    word_guess = input("You have used all of your letter guesses please guess the full word : ")
    word_guess.lower()
    if word_guess == word:
        print("YES the word was " + word_guess.capitalize() + " You WIN!")
        quit()
    else:
        print("No the word is not " + word_guess.capitalize() + " please try again.")
        wordGuess()


while current != word and lives > 0:

    print("You have %d lives left" % lives)
    guess = input("Please input one letter you have " + str(lives) + " letter guesses :\n----->")
    guess = guess.lower()

    if guess in guessed:
        print("You have already guessed this letter, please try again.")

    guessed.append(guess)

    if guess in word:
        indices = find_all(word, guess)
        x = list(current)
        hangman[lives]
        for i in indices:
            x[i] = guess
            current = "".join(x)
            print("Correct! \nYour guesses: %s" % (guessed))

            print(x)


    else:
        print("Incorrect, try again")
        lives = lives - 1
        print(hangman[lives])
        print(lives)
    if lives == 0:
        wordGuess()
        print(x)
if current == word:
    print("Well done, you have won!")

if __name__ == '__main__':
    print()
