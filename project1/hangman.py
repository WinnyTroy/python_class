# Name:
# MIT Username:
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
secret_word = ''  # Change this
letters_guessed = []

# From part 3b:


def word_guessed(text):
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    if text in letters_guessed:
        print "You already guessed" + text
    elif len(text) == len(word):
        letters_guessed.append(text)
    if text == word:
        return True
    else:
        print "Sorry that is incorrect."


def print_guessed(word, text):
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet.
    '''
    global secret_word
    global letters_guessed
    status = ''
    matches = 0

    for letter in word:
        if letter in letters_guessed:
            status += letter
        else:
            status += '*'
        if letter == text:
            matches += 1

    if matches > 1:
        print "Yes, the word contains", matches, " ", + text, "'s"
    elif matches == 1:
        print "Yes, the word contains the letter", text
    else:
        print "Sorry, the word does not contain the letter", text

    return status


def play_hangman():
    # Actually play the hangman game
    word = get_word()
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this
    # function
    mistakes_made = 0
    guessed = False

    print "The word contains ", len(word), "letters"

    while not guessed:
        text = raw_input("Please enter one letter: ")
        text = text.upper()

        word_guessed(text)

        if len(text) == 1:
            letters_guessed.append(text)
            result = print_guessed(word, text)

            if result == word:
                guessed = True
            else:
                print result
        else:
            print "Invalid Entry"
    print "Yes, the word is", word

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    return None


play_hangman()
