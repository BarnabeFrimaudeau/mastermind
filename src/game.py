from mastermind import *

if __name__ == '__main__':
    
    SIZE = 4
    TRIES = 10
    # green, red, blue, yellow, orange, purple
    VALID_CHARS = 'GRBYOP'
    
    code = create_code(VALID_CHARS, SIZE)
    user_guesses = []
    clues_list = []

    for i in range(10):
        # User input
        while True:
            user_guess = list(input('Please enter your guess of length ' + str(SIZE) + ' using the letters ' + str(VALID_CHARS) + ': '))
            
            if not valid(user_guess, VALID_CHARS, SIZE):
                pass
            else:
                user_guesses.append(user_guess)
                break

        # Check for clues
        clues = []

        for j in find_fully_correct(code, user_guess):
            clues.append(j)
        for j in find_colour_correct(remove_fully_correct(code, user_guess), user_guess):
            clues.append(j)

        clues_list.append(clues)

        print(code)
        print(display_game(user_guesses, clues_list))

        if clues == ['b', 'b', 'b', 'b']:
            print("Congratulations! It took you " + str(i + 1) + " attempts to find the code.")
            break
        elif i == 9:
            print("I'm sorry you lose. The correct code was " + str("".join(code)))
            break