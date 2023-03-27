import random

def create_code(characters, length):
    ''' Creates a randomly generated code from a list with a restricted length.
    characters = 'ABC'
    length = 4
    >>> ACAB
    '''
    code_generated = []

    for i in range(length):
        code_generated.append(random.choice(list(characters)))
    
    return code_generated

def find_fully_correct(answer, guess):
    ''' Returns 'b' for each number of correctly positioned colors in the guess.
    answer = ['P', 'G', 'R', 'O']
    guess = ['Y', 'G', 'O', 'O']
    >>> ['b', 'b']
    answer = ['P', 'G', 'R', 'O']
    guess = ['P', 'G', 'R', 'O']
    >>> ['b', 'b', 'b', 'b']
    '''
    correctly_positioned_colors = []

    for i in range(len(answer)):
        if answer[i] == guess[i]:
            correctly_positioned_colors.append('b')

    return correctly_positioned_colors

def remove_fully_correct(list1, list2):
    ''' Returns a list that removed every correctly positioned valid guesses.
    list1 = ['A', 'B', 'C', 'D']
    list2 = ['D', 'B', 'A', 'D']
    >>> ['A', 'C']
    list1 = ['A', 'B', 'Y', 'G']
    list2 = ['A', 'Y', 'Y', 'G']
    >>> ['B']
    '''
    not_fully_correct = []

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            not_fully_correct.append(list1[i])

    return not_fully_correct

def remove_fully_correct_from_guess(list1, list2):
    ''' Returns a list that removed every correctly positioned valid guesses.
    list1 = ['A', 'B', 'C', 'D']
    list2 = ['D', 'B', 'A', 'D']
    >>> ['D', 'A']
    list1 = ['A', 'B', 'Y', 'G']
    list2 = ['A', 'Y', 'Y', 'G']
    >>> ['Y']
    '''
    not_fully_correct = []

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            not_fully_correct.append(list2[i])

    return not_fully_correct

def find_colour_correct(answer, guess):
    ''' Returns a 'w' for each unique strings that are correct but not in the right place.
    answer = ['Y', 'P', 'G', 'G']
    guess = ['G', 'P', 'O', 'R']
    >>> ['w']
    answer = ['G', 'B', 'G', 'Y']
    guess = ['B', 'B', 'Y', 'G']
    >>> ['w', 'w', 'w']
    '''
    incorrect_position = []

    for i in guess:
        if i in answer:
            incorrect_position.append('w')
            answer[answer.index(i)] = ''

    return incorrect_position

def display_game(guesses, clues):
    """ Displays the current guesses and clues
    guesses = [['Y', 'P', 'G', 'G'], ['O', 'O', 'G', 'G']]
    clues = [['b', 'b'], ['b', 'b', 'b', 'b']]
    >>> '''
        Guess    Clues
        ****************
        Y P G G  b b
        O O G G  b b b b 
        '''
    """
    current_state = 'Guess\tClues\n****************\n'

    for i in range(len(guesses)):
        condensed_letters = ' '.join(guesses[i])
        b_to_print = ' '.join(clues[i])
        new_state = condensed_letters + '\t' + b_to_print + '\n'
        current_state += new_state

    return current_state

def valid(user_guess, valid_characters, guess_size):
    ''' Returns False if the input breaks any rules
    user_guess = ['A', 'B', 'C', 'X']
    valid_characters = 'GRBYOP'
    guess_size = 4
    >>> False
    '''
    for i in range(guess_size):
        if user_guess[i] not in valid_characters:
            return False
    
    return True