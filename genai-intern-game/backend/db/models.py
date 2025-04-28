from collections import deque

global_counts = {}
guess_list = deque(maxlen=50)

def update_guess_counter(guess):
    global global_counts
    if guess not in global_counts:
        global_counts[guess] = 0
    global_counts[guess] += 1
    return global_counts[guess]

def check_duplicate(guess):
    return guess in guess_list

def add_guess_to_list(guess):
    guess_list.append(guess)