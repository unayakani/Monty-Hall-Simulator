import random

wins = int()
losses = int()

for x in range(100):
    cases = [
            ['Goat', 'Goat', 'Car' ],
            ['Goat', 'Car' , 'Goat'],
            ['Car' , 'Goat', 'Goat' ],
            ]

    random_case = random.randrange(0, 3)

    case = cases[random_case]

    player_choice = random.randrange(0, 3)

    remove_door = random.randrange(3)

    while remove_door == player_choice or case[remove_door] == 'Car':
        remove_door = random.randrange(3)

    switch_choice = 3 - player_choice - remove_door

    player_choice = switch_choice

    if case[player_choice] == 'Car':
        wins += 1
    else:
        losses += 1

percentage_win = (wins / (wins + losses)) * 100

print(percentage_win)

# -------------
'''
    remove_door = int()

    while True:
        remove_door = random.randrange(0, 3)
        if remove_door == player_choice or case[remove_door] == 'Car':
            continue
        else:
            break

    case.pop(remove_door)

    if player_choice == 0:
        player_choice = 1
    else:
        player_choice = 0
'''
