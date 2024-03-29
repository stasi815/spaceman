"""Spaceman."""
import random

# Color selection


def prRed(skk):
    """Red."""
    return("\033[91m {}\033[00m" .format(skk))


def prGreen(skk):
    """Green."""
    return("\033[92m {}\033[00m" .format(skk))


def prYellow(skk):
    """Yellow."""
    return("\033[93m {}\033[00m" .format(skk))


def prLightPurple(skk):
    """Light Purple."""
    return("\033[94m {}\033[00m" .format(skk))


def prPurple(skk):
    """Purple."""
    return("\033[95m {}\033[00m" .format(skk))


def prCyan(skk):
    """Cyan."""
    return("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk):
    """Light Gray."""
    return("\033[97m {}\033[00m" .format(skk))


def prBlack(skk):
    """Black."""
    return("\033[98m {}\033[00m" .format(skk))


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


# # help from Jessica Trinh and https://stackoverflow.com/questions/12971474/
# /how-to-find-if-a-secret-word-contains-all-the-characters-from-a-words_list

# TODO: Loop through the letters in the secret_word and check if a letter
# is not in letters_guessed
# pass

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
    return print(prCyan(word_progress))


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
    # TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

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

    # TODO: show the player information about the game according to the
    # project spec:
    print(prCyan(
        """
 __        __   _                            _
 \\ \\      / /__| | ___ ___  _ __ ___   ___  | |_ ___
  \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | __/ _ \\
   \\ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |
    \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___|  \\__\\___/
  ____
 / ___| _ __   __ _  ___ ___ _ __ ___   __ _ _ __
 \\___ \\| '_ \\ / _` |/ __/ _ \\ '_ ` _ \\ / _` | '_ \\
  ___) | |_) | (_| | (_|  __/ | | | | | (_| | | | |
 |____/| .__/ \\__,_|\\___\\___|_| |_| |_|\\__,_|_| |_|
       |_|
            Spaceman is a friendlier, less morbid version of the classic game
            'hangman.' You have 7 incorrect guesses per game. Please enter one
            letter per guess! Have fun!"""))
    print(prLightPurple("The secret word has " + len_secret_word + " letters"))
    print(prYellow("-----------------------"))

    while total_guesses > 0 and is_word_guessed(
                secret_word, letters_guessed) is False:
        guessed_word is False
        #  Thanks George Aoyogi
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            guessed_word = False
            break
        # TODO: Ask the player to guess one letter per round and check that
        # it is only one letter:
        print(prPurple((
            "You have ") + str(total_guesses) + (" incorrect guesses left.")))
        guess = input(prRed("Enter a single letter: ")).lower()

        if guess in secret_word:
            # TODO: Check if the guessed letter is in the secret or not and
            # give the player feedback:
            if guess in letters_guessed:
                print(
                    """You already guessed that letter: """)
                # TODO: show the guessed word so far
                get_guessed_word(secret_word, letters_guessed)
                print(prYellow("-----------------------"))
            else:
                letters_guessed.append(guess)
                print(
                    prYellow("Your letter is in the secret word!") + prGreen(
                        "wOo!"))
                get_guessed_word(secret_word, letters_guessed)
                print(prYellow("-----------------------"))
        else:
            if guess in letters_guessed:
                print("""You already guessed that letter: """)
                get_guessed_word(secret_word, letters_guessed)
                print(prYellow("-----------------------"))
            else:
                letters_guessed.append(guess)
                total_guesses -= 1
                print(
                    """Your letter is not in the secret word. Try again!""")
                get_guessed_word(secret_word, letters_guessed)
                print(prYellow("-----------------------"))

    # TODO: check if the game has been won or lost
    if is_word_guessed(secret_word, letters_guessed):
        print(prGreen("""You guessed the secret word!
 __   __                     _       _
 \\ \\ / /__  _   _  __      _(_)_ __ | |
  \\ V / _ \\| | | | \\ \\ /\\ / / | '_ \\| |
   | | (_) | |_| |  \\ V  V /| | | | |_|
   |_|\\___/ \\__,_|   \\_/\\_/ |_|_| |_(_)

"""))
        print(prYellow(secret_word))
        
    else:
        total_guesses == 0
        print(
                prRed(
                    """
  _   _ _             _     _
 | | | | |__     ___ | |__ | |
 | | | | '_ \\   / _ \\| '_ \\| |
 | |_| | | | | | (_) | | | |_|
  \\___/|_| |_|  \\___/|_| |_(_)

 You lost this round. Please play again.The secret
                    word was: """))
        print(prLightPurple(secret_word))
       



# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)

