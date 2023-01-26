import random
from words import words
import string

#Selects a Valid Word Without Spaces and Hyphens
def valid_word(words):
    found = False
    word = random.choice(words)

    while found != True:
        if word.__contains__('-') or word.__contains__(' '):
            word = random.choice(words)
        else:
            found = True
    return word.upper()

#Main Game Function
def hangman():
    word = valid_word(words) # Gets a Valid Word
    word_letters = set(word) # Converts the Word in a Set of Letters
    alphabets = set(string.ascii_uppercase) # Set of Alphebets
    used_letters = set() # Set of Letters Used by the User Already
    lives = 6 # Total Lives / Chances

    while len(word_letters) > 0 and lives != 0:
        print("\nLetters You Have Used: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word] # Prints the Letters of the Words Which The User has Guessed Correctly Otherwise a Hyphen
        print('WORD: ', ' '.join(word_list)) # Prints the Word Separated by Spaces
        print('LIVES = ', lives)

        user_letter = input('Enter a Letter: ').upper() # Input By The User in Form of Single Character

        if user_letter in alphabets - used_letters: # Checks If the Character is not in Letters Already Entered by the User and is a Valid Alphabet
            used_letters.add(user_letter) # Adds the Letter to the Used Letter Set
            if user_letter in word_letters: # If the Letter is Present in the Word
                word_letters.remove(user_letter) # Remove the Letter from Set of Word Letters
            else:
                lives -= 1 # If the Letter is Not in Word, Remove a Life
                print("\nLetter is Not in Word!\n")
        
        elif user_letter in used_letters: # If User has Already Entered That Letter
            print("You Have Already Used This Letter!\n")

        else:
            print("Wrong Character!")
    
    if lives == 0:
        print('You Lost! The Word Was: ', word.upper())
    else:
        print('You Won! The Word Was: ', word.upper())


hangman()