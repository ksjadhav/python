import random

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

WORDS = 'python hangman challenge program computer science code'.split()

def get_random_word(word_list):
    return random.choice(word_list)

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()
    print('Missed letters:', ' '.join(missed_letters))
    blanks = ['_' if letter not in correct_letters else letter for letter in secret_word]
    print(' '.join(blanks))
    print()

def get_guess(already_guessed):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Try again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess

def play_again():
    return input('Do you want to play again? (yes or no): ').lower().startswith('y')

def main():
    print('H A N G M A N')
    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(WORDS)
    game_is_done = False

    while True:
        display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess
            found_all_letters = all(letter in correct_letters for letter in secret_word)
            if found_all_letters:
                print(f'Yes! The secret word is "{secret_word}"! You have won!')
                game_is_done = True
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print(f'You have run out of guesses!\nAfter {len(missed_letters)} missed guesses and {len(correct_letters)} correct guesses, the word was "{secret_word}".')
                game_is_done = True

        if game_is_done:
            if play_again():
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word(WORDS)
                game_is_done = False
            else:
                break

if __name__ == '__main__':
    main()      
    # This code implements a simple Hangman game in Python.
    # The player guesses letters to figure out a secret word, with a limited number of incorrect guesses allowed.
    # The game continues until the player either guesses the word or runs out of attempts.
    # The player can choose to play again after finishing a game.
    # The game uses a list of predefined words and displays the hangman state based on the number of incorrect guesses.
# The game is interactive, prompting the player for input and providing feedback on their guesses.  ie