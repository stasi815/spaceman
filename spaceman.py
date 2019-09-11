"""Spaceman."""
import random

letters_guessed = []
# makes and stores list of letters that user guessed into array


def load_word():
    """Load secret word."""
    """
    Function that loads the secret word.

    A function that reads a text file of words and randomly
    selects one to use as the secret word from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game.

    """
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

# User Input
# def user_input(prompt):
#    """Accept user input."""
    # the input function will display a message in the terminal
    # and wait for user input.
#   user_input = input(prompt)
#  return user_input
    # user_value = user_input("Please Enter a value:")
    # print(user_value)


def is_word_guessed(secret_word, letters_guessed):
    """Check if all letters were guessed."""
    """

    Function that checks if all the letters of the secret word have
    been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in
        letters_guessed, False otherwise

    """
# https://stackoverflow.com/questions/12971474/
# how-to-find-if-a-secret-word-contains-all-the-characters-from-a-words_list
    # return set(secret_word) <= set(letters_guessed)
    # TODO: Loop through the letters in the secret_word and check if a letter
    # is not in letters_guessed
    pass
    # help from Jessica Trinh
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        return True


def get_guessed_word(secret_word, letters_guessed):
    """Get the guessed word."""
    """

    Function that is used to get a string showing the letters guessed so far in
    the secret word and underscores for letters that have not been guessed yet.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been
        guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user
        has guessed correctly, the string should contain the letter at the
        correct position.  For letters in the word that the user has not yet
        guessed, shown an _ (underscore) instead.

    """

# TODO: Loop through the letters in secret word and build a string that
# shows the letters that have been guessed correctly so far that are saved
# in letters_guessed and underscores for the letters that have
# not been guessed yet


# pass

    word_progress = " "

    for letter in secret_word:
        if letter in letters_guessed:
            word_progress += letter
        else:
            word_progress += "_"
    return print(word_progress)


def is_guess_in_word(guess, secret_word):
    """Check if guessed letter is in word."""
    """
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    """

    if guess in secret_word:
        return True
    else:
        return False
    # TODO: check if the letter guess is in the secret word

    # pass


def spaceman(secret_word):
    """Control spaceman game."""
    """
    A function that controls the game of spaceman. Will start spaceman in the
    command line.
    Args:
      secret_word (string): the secret word to guess.

    """
    # https://www.youtube.com/watch?v=fSZDfGXWD4M
    # https://gist.github.com/saltavenger/3939185
    letters_guessed = []
    len_secret_word = str(len(secret_word))
    total_guesses = 7
    guess = " "
    guessed_word = False

    print("Welcome to Spaceman. A friendlier, less morbid version of the"
            " classic game 'hangman.'You have 7 incorrect guesses per game,"
            " please enter one letter guess per guess! Have fun!")
    print("The secret word has " + len_secret_word + " letters.")
    print("-----------------------")

    while total_guesses > 0 and total_guesses <= 8 and guessed_word is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            guessed_word = True
            break
        print("You have " + str(total_guesses) + " incorrect guesses left.")
        guess = input("Enter a single letter: ").lower()
        if guess in secret_word:
            if guess in letters_guessed:
                print(
                    "You already guessed that letter"
                    ": ")
                get_guessed_word(secret_word, letters_guessed)
                print("-----------------------")
            else:
                letters_guessed.append(guess)
                print(
                    "Your letter is in the secret word! wOo!"
                    "")
                get_guessed_word(secret_word, letters_guessed)
                print("-----------------------")
        else:
            if guess in letters_guessed:
                print(
                    "You already guessed that letter"
                    ": ")
                get_guessed_word(secret_word, letters_guessed)
                print("-----------------------")
            else:
                letters_guessed.append(guess)
                total_guesses -= 1
                print(
                    "Your letter is not in the secret word. Try again"
                    "!")
                get_guessed_word(secret_word, letters_guessed)
                print("-----------------------")

        if guessed_word is True:
            return "You guessed the secret word! You win!"
        elif total_guesses == 0:
            print("Uh oh! You lost this round. Please play again. The secret\
            word was: ") + secret_word

    # TODO: show the player information about the game according to the
    # project spec:

    # "Welcome to Spaceman. A friendlier, less morbid version of the classic
    # game 'hangman.'"
    # "The secret word contains: 6 letters"
    # "You will have 7 incorrect guesses, please enter a one letter guess
    # per round!"
    # "Have fun!"

    # TODO: Ask the player to guess one letter per round and check that it is
    # only one letter:

    # "Enter a letter: "
    # "Please enter a single letter at a time."

    # TODO: Check if the guessed letter is in the secret or not and give
    # the player feedback:

    # "Your letter is in the secret word! wOo!"
    # "You haven't guessed these letters yet, keep trying!: "
    # "Your letter is not in the secret word. Try again!"
    # "You have 6 incorrect guesses left."
    # "You have 5 incorrect guesses left."
    # "You have 4 incorrect guesses left."
    # You have 3 incorrect guesses left."
    # "You have 2 incorrect guesses left."
    # "You have only 1 incorrect guess left!"

    # TODO: show the guessed word so far
    # "Guessed word so far: "
    # TODO: check if the game has been won or lost
    # "Uh oh! You lost this round. Please play again."
    # "You guessed the secret word! You win!"


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
