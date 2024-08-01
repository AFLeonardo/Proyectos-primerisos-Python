from random import * 
import time, os
# VARIBLES
guess_words = [
    "Avatar",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Creed",
    "Pulp Fiction",
    "Forrest Gump",
    "Rocky",
    "Matrix",
    "The Silence of the Lambs"
]

Incorrect_letters = []

# FUNCTIONS
def Only_one(answer):
    while len(answer) != 1:
        print("*** \nWRONGG!! \nONLY ONE LETTER IS ALLOWED \n***")
        answer = input("\nInput one letter: ").lower()

def Tell_me_letter():
    answer = input("Input one letter: ").lower()
    # Verificate to answer to only one letter.
    Only_one(answer)
    return answer

def Not_Spaces_Word(word):
    New_word = word.replace(" ","")
    return New_word

def Change(word, answer, secret_word):
    answer = answer.lower()
    positions = [i for i, letter in enumerate(word) if letter == answer]
    for position in positions:
        secret_word[position] = answer
    return secret_word

"************************************************************"

word = choice(guess_words).lower()
word = Not_Spaces_Word(word)
secret_word = list("_" * len(word))

Lifes = 6
while Lifes > 0:
    print(f"LIFES {Lifes}")
    print("\nGuess the word \n", "  ".join(secret_word), "\n")

    answer = Tell_me_letter()
    os.system("cls")

    if answer in word:
        secret_word = Change(word, answer, secret_word)
        if "_" not in secret_word:
            print("Congratulations! You've guessed the word:", "".join(secret_word))
            break

    else:
        time.sleep(1)
        print("WRONG, the letter is not in the word. \nTry again")
        time.sleep(1)
        os.system("cls")
        Incorrect_letters.append(answer)
        print(f"Incorrect letters: {Incorrect_letters}")
        Lifes -= 1

time.sleep(2)
if Lifes == 0:
    print(f"You kill the monkey. YOU FAIL. \nThe correct word was {word}")