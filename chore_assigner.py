import random

roommates = []
chores = []

def get_roommate_names():
    print("Hello, welcome to the chore assignment management program!")
    while True:
        name = input('Enter the names of your roommates (type \'done\' to finish): ').strip().lower()
        if name == 'done':
            break
        if name: # Only add if not empty
            roommates.append(name)

def get_chore_list():
    while True:
        chore_name = input('List the chores to be done one by one (type \'done\' to finish): ').strip().lower()
        if chore_name == 'done':
            break
        if chore_name: # Only add if not empty
            chores.append(chore_name)

get_roommate_names()
get_chore_list()

print('\nHere are the assigned chores:')
if not roommates or not chores:
    print("Error: The list of roommates or chores is empty.")
else:
    for chore in chores:
        # Randomly choose a person for each chore
        assigned_roommate = random.choice(roommates)
        print(f'{chore.capitalize():<20} -> assigned to: {assigned_roommate.capitalize()}')
