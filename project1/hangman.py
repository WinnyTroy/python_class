import random


def get_word():
    words = ['choose', 'list', 'iran', 'behboudi', 'italia',
             'instagram', 'facebook', 'war', 'likeit', 'motivation', 'crazy',
             'dirty', 'love', 'hate', 'trump', 'who', 'mom', 'water', 'torta',
             'kill', 'no', 'fardin']
    return random.choice(words).upper()


def check_word(word, guesses, guess):
    guess = guess.upper()
    status = ''
    i = 0
    matches = 0

    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'

        if letter == guess:
            matches += 1

    if matches > 1:
        print 'Yes, the word contains', matches, '"' + guess + '"' + 's'
    else:
        print 'Sorry, the word does not contain the letter', +guess

    return status



def main():
	pass
