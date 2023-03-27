from mastermind import *

if __name__ == "__main__":

    SIZE = 4
    TRIES = 10
    VALID_CHARS = "GRBYOP"

    code = create_code(VALID_CHARS, SIZE)
    user_guesses = []
    clues_list = []
    
    for i in range(TRIES):
        while True:
            user_guess = list(input("Please enter your guess of length " + str(SIZE) + " using the letters " + str(VALID_CHARS) + ": "))
            
            if valid(user_guess, VALID_CHARS, SIZE):
                user_guesses.append(user_guess)
                break
            else: pass

        clues = []
        rmv_fully_correct_code, rmv_fully_correct_guess = remove_fully_correct(code, user_guess)

        for j in find_fully_correct(code, user_guess):
            clues.append(j)
        for j in find_colour_correct(rmv_fully_correct_code, rmv_fully_correct_guess):
            clues.append(j)

        clues_list.append(clues)

        print(display_game(user_guesses, clues_list))

        if clues == ["b", "b", "b", "b"]:
            print("Congratulations! It took you " + str(i + 1) + " attempts to find the code.")
            break
        elif i == 9:
            print("I'm sorry you lose. The correct code was " + str("".join(code)))
            break