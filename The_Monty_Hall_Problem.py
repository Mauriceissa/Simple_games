import random
import time

# Initialize score variables
same_door_win_score = 0
switch_door_win_score = 0
same_door_lose_score = 0
switch_door_lose_score = 0

# Function to check if the player wants to continue playing
def keepPlaying():
    # Prompt user for input
    keep_playing = input('Do you want to play again?\n("yes"/"no")\n\n->').lower()

    if keep_playing == 'yes':
        return True
    else:
        print('Thanks for playing!')
        return False

# Main loop control variable
loopa = True

# Main game loop
while loopa:
    # Initialize the doors with two goats and a car
    doors = ["Goat", "Goat", "Car"]
    door_nr = [1,2,3]

    # Shuffle the doors randomly
    random.shuffle(doors)

    # Create a dictionary of door numbers and their respective contents
    door_dict = {nr: door for nr, door in zip(door_nr,doors)}
    Door_goat = [key for key, value in door_dict.items() if value == 'Goat']
    Door_car = [key for key, value in door_dict.items() if value == 'Car']

    # Print the player's current score
    print(f'When keeping the same door:\nYou won {same_door_win_score}\nYou lost {same_door_lose_score}')
    print(f'When switching the door:\nYou won {switch_door_win_score}\nYou lost {switch_door_lose_score}')
    print()

    try:
        # Accept user's initial door choice
        guess = int(input('Write a number between 1-3 to choose between:\nDoor number [1]\nDoor number [2]\nDoor number [3]\n\n->'))
        if guess in door_nr:
            if guess in Door_goat:
                Door_goat.remove(guess)
                print(f'You chose door number {guess}')
                time.sleep(2)
                print(f'Door {Door_goat} contains a goat\n')
                time.sleep(1)
                
                # Offer the player a chance to switch their chosen door
                choice = input(f'Now, knowing that there is a goat in {Door_goat},\nwould you like to change your door to door number {Door_car}\n("yes"/"no")\n\n->').lower()

                if choice == 'yes':
                    guess = Door_car
                    time.sleep(1)
                    print(f'You chose to change to door nr {guess}\n')
                    print(door_dict)
                    print()
                    switch_door_win_score +=1
                    print(f'You win!!\nYour score when changing door is {switch_door_win_score}')
                    loopa = keepPlaying()
                else:
                    print(f'The car was behinde door {Door_car}\nYou chose not to change to door nr {Door_car}\n')
                    print(door_dict)
                    print()
                    print(f'You lost!!\nYour score when keeping the same door is {same_door_win_score}')
                    same_door_lose_score +=1
                    loopa = keepPlaying()

            else:
                print(f'You chose door number {guess}')
                time.sleep(2)
                print(f'Door {Door_goat[0]} contains a goat\n')
                
                # Offer the player a chance to switch their chosen door
                choice = input(f'Now, knowing that there is a goat in {Door_goat[0]},\nwould you like to change your door to door number {Door_goat[1]}\n("yes"/"no")\n\n->').lower()
                
                if choice == 'yes':
                    guess = Door_goat[1]
                    time.sleep(2)
                    print(f'You chose to change to door nr {guess}\n')
                    print(door_dict)
                    print()
                    print(f'You lost!!\nYour score when keeping the same door is {switch_door_win_score}')
                    switch_door_lose_score +=1
                    loopa = keepPlaying()
                else:
                    time.sleep(2)
                    print(f'You chose not to change to door nr {Door_goat[1]}\n')
                    print(door_dict)
                    print()
                    same_door_win_score +=1
                    print(f'You win!!\nYour score when changing door is {same_door_win_score}')
                    loopa = keepPlaying()
        else:
            # Handle invalid door number input
            print('You can only enter a number between 1-3 (corresponding to door 1 - door 3 )')
            time.sleep(2)
            print('Try again!')
            time.sleep(1)
            continue

    except ValueError:
        # Handle non-integer input
        print('You can only enter a number between 1-3 (corresponding to door 1 - door 3 )')
        time.sleep(3)
        print('Try again!')
        time.sleep(1)
