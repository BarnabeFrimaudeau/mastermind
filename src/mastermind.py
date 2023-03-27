import random
import os


def create_code(characters, length):
    '''Generate a random 4 letter code from 6 avaiable letters.'''
    code_generated = []

    for i in range(length):
        code_generated.append(random.choice(list(characters)))

    return code_generated


def find_fully_correct(answer, guess):
    '''Output a 'b' for every guessed colors that are in the correct postition.
    >>> find_fully_correct(['Y', 'B', 'B', 'R'], ['B', 'B', 'Y', 'P'])
    ['b']
    >>> find_fully_correct(['B', 'P', 'G', 'R'], ['G', 'P', 'G', 'R'])
    ['b', 'b', 'b']
    '''
    correctly_positioned_colors = []

    for i in range(len(answer)):
        if answer[i] == guess[i]:
            correctly_positioned_colors.append("b")

    return correctly_positioned_colors


def remove_fully_correct(list1, list2):
    '''Output a new list composed of colors which are not correctly positioned.
    >>> remove_fully_correct(['Y', 'B', 'B', 'R'], ['B', 'B', 'Y', 'P'])
    ['Y', 'B', 'R'], ['B', 'Y', 'P']
    >>> remove_fully_correct(['B', 'P', 'G', 'R'], ['G', 'P', 'G', 'R'])
    ['B'], ['G']
    '''
    not_fully_correct_code = []
    not_fully_correct_guess = []

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            not_fully_correct_code.append(list1[i])
            not_fully_correct_guess.append(list2[i])    

    return not_fully_correct_code, not_fully_correct_guess


def find_colour_correct(answer, guess):
    '''Output a 'w' for every incorrectly positioned colors that exist in the
    answer.
    >>> find_colour_correct(['Y', 'B', 'B', 'R'], ['B', 'B', 'Y', 'P'])
    ['w', 'w']
    >>> find_colour_correct(['B', 'P', 'G', 'R'], ['G', 'P', 'G', 'R'])
    []
    '''
    incorrect_position = []

    for i in guess:
        if i in answer:
            incorrect_position.append("w")
            answer[answer.index(i)] = ""

    return incorrect_position


def display_game(guesses, clues):
    '''Every attempt, show the current and past attempts as well as the clues
    outputted for each.'''
    current_state = "Guess\tClues\n****************\n"
    os.system("cls")

    for i in range(len(guesses)):
        condensed_letters = ' '.join(guesses[i])
        b_to_print = ' '.join(clues[i])
        new_state = condensed_letters + "\t" + b_to_print + "\n"
        current_state += new_state

    return current_state


def valid(user_guess, valid_characters, guess_size):
    '''Make sure that the input respects the game rules.
    >>> valid(['B', 'B', 'Y', 'P'], "GRBYOP", 4)
    True
    >>> valid(['5', 'A', 'D', 'Y', 'P', 'R'], "GRBYOP", 4)
    False
    '''
    if len(user_guess) == guess_size:
        for i in range(guess_size):
            if user_guess[i] not in valid_characters:
                return False
    else: return False

    return True