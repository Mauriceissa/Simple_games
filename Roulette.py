import random as rdm    # Import the necessary libraries. 'rdm' is an alias for the random library.
import time             # I have imprted time to use the sleep function that makes the program paus. I have done this for readability and dramatic reasons in this code

# Tupel of all red numbers on the roulette wheel.
Red_nr = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)

all_bets = {'Number bet': [],                           # Here i have crated a dict that will store all user bets.
            'Color bet' : {'color': None,'color bet size': None },
            'Dozen bet' : [],
            'neighbour bet': []}

Dozen_bet_1 = (1,2,3,4,5,6,7,8,9,10,11,12)              # Tupels of dozens for betting.
Dozen_bet_2 = (13,14,15,16,17,18,19,20,21,22,23,24)
Dozen_bet_3 = (25,26,27,28,29,30,31,32,33,34,35,36)

Balance=500       # Initial balance for the player.
Past_result = []  # List to store past results.

last_betting_number = [] # Variables to store last bets made by the player.
last_betting_color = None
last_betting_color_size = 0
last_betting_dozen = None

# Dictionary of numbers and their neighbours on the roulette wheel.
neighbours = {0: [26, 32], 1: [33, 20], 2: [21, 25], 3: [35, 26], 4: [19, 21], 5: [10, 24], 6: [34, 27], 7: [29, 28], 8: [30, 23], 9: [31, 22], 10: [23, 5], 11: [36, 30],
             12: [28, 35], 13: [27, 36], 14: [20, 31], 15: [32, 19], 16: [24, 33], 17: [25, 34], 18: [22, 29], 19: [15, 4], 20: [1, 14], 21: [4, 2], 22: [9, 18], 23: [8, 10],
             24: [5, 16], 25: [2, 17], 26: [3, 0], 27: [6, 13], 28: [7, 12], 29: [18, 7], 30: [11, 8], 31: [14, 9], 32: [0, 15], 33: [16, 1], 34: [17, 6], 35: [12, 3], 36: [13, 11]}

def Play():  # This function simulates the rolling of the roulette wheel and determines the winnings or losses.
    global Balance
    global winnings          # Access the global variables to update the player's balance, winnings, and loss/profit globally.
    global loss_profit
    
    print('Lycka till!!')
    roulett_nr = rdm.randint(0,36) # Randomly generate a roulette number between 0 and 36.
        
    time.sleep(3)     # Create a dramatic pause before revealing the result of the roulette spin.
    print('Resultat kommer om 3') 
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

    if roulett_nr == 0:  # If the random number is 0, the color is green.
        färg = 'Grön'
    elif roulett_nr in Red_nr: # Check if the random number is in the Red_nr list, if so, the color is red.
        färg = 'Rött'
    else:
        färg = 'Svart' # If the number is not 0 or in the Red_nr list, the color is black.

    # Check if the number is within 1-12, 13-24, or 25-36.
    
    if 1 <= roulett_nr <= 12:
        Del = 'del 1'
    elif 13 <= roulett_nr <= 24:
        Del = 'del 2'
    elif 25 <= roulett_nr <= 36:
        Del = 'del 3'
    
    Past_result.append((roulett_nr, färg, Del))   # Store the result of this spin for reference.

    print(f'Kulan hamnade på nummer {roulett_nr} {färg} i {Del}\n')  # Print where the ball landed (number/color/section).
    time.sleep(2)
    winnings = 0
    for bett_nr in all_bets['Number bet']: # Loop through all number bets.
        
        if roulett_nr == bett_nr['number']: # Check if any of the bets match the number the ball landed on.# Kollar om någon av betten matchar med nr kulan landa på
            winnings += (betting_size * 36)

    if färg.upper() == all_bets['Color bet']['color']: # Check if the color the ball landed on matches a color bet.
        winnings += (color_bet_size * 2)

    for i in all_bets['Dozen bet']:
        if roulett_nr in i['dozen number']:
            winnings += i['dozen bet size'] * 2
    
    for bet in all_bets['neighbour bet']:
        if roulett_nr == bet['numbers']:
            winnings += bet['neighbour number bet size'] * 36

            
    Balance += winnings                  # Add potential winnings to the balance.
    total_bet = total_bet_size()         # Calculate the total amount the player has bet this round.
    loss_profit = winnings - total_bet   # Calculate the net gain or loss.
    
    return Balance, winnings, loss_profit

def Your_plays():# This function displays all the current bets made by the player.

    print('Dina spel är:\n')
    
    if len(all_bets['Number bet']) != 0:                             # Checking if there are any number bets placed by the player.
        print('\tDina spelade nummer är:')
        
        for bet in all_bets['Number bet']:                           # Iterating through each number bet placed and printing the details.
            print(f'\n\tNR:{bet["number"]}- - -{bet["bet size"]}kr') # Displaying the bet number and amount.
    else:
        print('\t---------------\n\tInga nummer spelade än ännu\n')  # Message indicating no number bets have been placed.

                                                                     # Checking if the player has placed any color bets.
    if all_bets["Color bet"]["color"] != None and all_bets["Color bet"]["color bet size"] !=0:
        print(f'\t---------------\n\tDu har spelat på färgen:\n\t{all_bets["Color bet"]["color"]}- - -{all_bets["Color bet"]["color bet size"]}')
    else:
        print('\tInga spel på färg än\n')
    
    if len(all_bets['Dozen bet']) != 0:                              # Checking if there are any dozen bets placed by the player.
        print(f'\t---------------\n\tDozen spel på Del:')
        
        for dozen in all_bets['Dozen bet']:                          # Iterating through each dozen bet placed and printing the details.
           print(f'\n\t{dozen["dozen number"]}- - - {dozen["dozen bet size"]}')
    else:
        print('\tInga spel på dozen än\n')

    if len(all_bets['neighbour bet']) != 0:                          # Checking if there are any neighbour bets placed by the player.
        print(f'\t---------------\n\tgrann spel är:')
        
        for neighbour in all_bets['neighbour bet']:
            print(f'\n\t{neighbour["numbers"]} - - - {neighbour["neighbour number bet size"]}')
    else:
        print('\tInga spel på grannar än\n')

    total_bet=total_bet_size()
    print(f'Din totala insatts är {total_bet}') # Displaying the total bet amount.
    
def Same_play():    # This function allows the player to repeat their last set of bets.

    global Balance

    all_bets['Number bet']=last_betting_number
    all_bets['Color bet']['color']=last_betting_color
    all_bets['Color bet']['color bet size']= last_betting_color_size
    all_bets['Dozen bet']=last_betting_dozen
    all_bets['neighbour bet']=last_betting_neighbour
    
    total_bet = total_bet_size()

    if total_bet <= Balance:
               
        print('Ditt förra spel spelats igen.')
        Balance = Balance - total_bet
        time.sleep(2)
        
    else: 
       print(f'Ditt saldo är för lågt för att spela samma spel igen.\nDitt saldo är {Balance}')
       Clear_Values()

def Check_balance(bet_amount):      # This function checks if the player's balance is sufficient for placing a bet.
    if Balance - bet_amount < 0:
        print("Ditt saldo är för lågt för att spela.")
        time.sleep(1)
        return False
    return True

def total_bet_size():   # This function calculates the total size of all current bets.

    total_number_bets_size = sum(bet['bet size'] for bet in all_bets['Number bet']) if all_bets['Number bet'] else 0
    total_color_bets_size = all_bets['Color bet']['color bet size'] if all_bets['Color bet']['color bet size'] else 0
    total_dozen_bets_size = sum(bet['dozen bet size'] for bet in all_bets['Dozen bet']) if all_bets['Dozen bet'] else 0
    total_neighbour_bets_size = sum(bet['neighbour number bet size'] for bet in all_bets['neighbour bet']) if all_bets['neighbour bet'] else 0

    # Summing up all the bets
    total_bet = total_number_bets_size + total_color_bets_size + total_dozen_bets_size + total_neighbour_bets_size

    return total_bet

def Clear_Values(): # This function clears all the current bets.
    global all_bets
    all_bets = {'Number bet': [],
                'Color bet' : {'color': None,'color bet size': None },
                'Dozen bet' : [],
                'neighbour bet': []}

loopa = True        # Main loop for the game where the player can choose different options to bet, roll the wheel, or exit.
while loopa == True:
    
    print("\t\t\t\t\n\033[91m" + "Välkommen till roulette bordet" + "\033[0m\n") # This makes the print in the color of red.
    print('\t\t\t\t\t\t\tFöregående resultat var')
    for nr, färg, Del in Past_result:
        print(f'\n\t\t\t\t\t\t\tNR:{nr}--{färg}--{Del}')
         
    print(f'\n\tVälj ett av följande spelval:\t\t\tSaldo {Balance}kr\n')     
    print('\tSpela på nummer: välj (1)\t                Spela på Rött eller Svart: välj (2)\n'
          '\tSpela på Dozen/en tredje del av bordet: (3)\tSpela på grannar: (4)\n'
          '\tKolla mina spel: (5)\t                        Spela samma Spel: (6)')
    
    try:
        game_mode = int(input('\n\t\t\t\t\tRULLA KULA: (7)\n\t\tSkriv ditt svar här:\t->'))
    except:
        print('Du kan enbart välja ett värde mellan 1-7... FÖRSÖK IGEN')
        time.sleep(2)
        Clear_Values()
        continue
       
    try:
        game_mode in [1,2,3,4,5,6,7]
    
    except:
        print('Du kan enbart välja ett värde mellan 1-7... FÖRSÖK IGEN')
        time.sleep(2)
        Clear_Values()
        continue

# Each game mode corresponds to a different type of bet or action.
# Option to place a bet on specific numbers.
    if game_mode == 1:
        spela = 'Y'             # The user is asked if they want to continue playing, initializing with 'Y' to enter the loop for the first time.
        while spela == 'Y':
        
            betting_nr = int(input('Vilket nummer vill du spela på?\n'))     # The user is prompted to enter the number they wish to bet on.
            
            if betting_nr <0 or betting_nr >36:                              # Checks if the entered number is valid (between 0 and 36).
                print('Du kan bara spela på siffror mellan 0-36')
                continue                                                     # If the number is not valid, it prompts the user to enter the number again.

                                                                            # The user is prompted to enter the size of their bet, showing their current balance.
            betting_size = int(input(f'Du har {Balance} att spela för, hur mycket vill du spela på nr {betting_nr}?\n'))
            
            if betting_size > Balance:                                       # Checks if the user has enough balance to make the bet.
                print(f'Du har inte {betting_size} kvar att spela med. Du har {Balance} kvar att spela med') 
                input('Tryck ENTER för att gå vidare')
                break                                                        # Exits the loop if the bet size exceeds the available balance.

            Balance = Balance - betting_size                                 # Deducts the bet size from the user’s current balance.
                # Records the user's bet (number and size) in the all_bets dictionary.                                                   
            all_bets['Number bet'].append({'number': betting_nr, 'bet size': betting_size})
                # Asks the user if they want to bet on another number or proceed to spin the roulette.
            spela = input('Vill du spela på ett till nummer?\nY/N\n').upper()
            if spela != 'Y':
                break                                                        # Exits the loop if the user decides not to place another bet.
# Option to place a bet on a color (red or black).           
    if game_mode == 2:
        # Prompt the user to place a bet on either Red or Black
        color_bet = input('vill du betta på Svart eller Rött?\n'
                    'Skriv in antingen svart eller rött\n').upper() 
        if color_bet == 'RÖTT':                     # If the player bets on Red Ask how much the player wants to bet on Red.
            color_bet_size = int(input(f'Hur mycket vill du spela på Rött för? Du har {Balance} kvar att spela med '))
            all_bets['Color bet']={'color': color_bet, 'color bet size': color_bet_size}  # Record the color bet in the all_bets dictionary.

            if not Check_balance(color_bet_size):   # Check if the player has enough balance to make the bet.
                input(f'Du har inte {color_bet_size} kvar att spela med. Du har {Balance} kvar att spela med\nTryck ENTER för att fortsätta')  
        
                continue                            # If not enough balance, go back to the beginning of the loop.
            Balance = Balance - color_bet_size      # Deduct the bet amount from the player’s balance.

        elif color_bet == 'SVART':                  # If the player bets on black Ask how much the player wants to bet on black.
            color_bet_size = int(input(f'Hur mycket vill du spela på Svart för? Du har {Balance} kvar att spela med '))
            all_bets['Color bet']={'color': color_bet, 'color bet size': color_bet_size}  # Record the color bet in the all_bets dictionary.

            if not Check_balance(color_bet_size):  # Check if the player has enough balance to make the bet.
                input(f'Du har inte {color_bet_size} kvar att spela med. Du har {Balance} kvar att spela med\nTryck ENTER för att fortsätta')               
                continue                           # If not enough balance, go back to the beginning of the loop.
            Balance = Balance - color_bet_size     # Deduct the bet amount from the player’s balance.
        else:
            continue                               # If the player enters something other than Black or Red, go back to the menu.
# Option to place a bet on dozens (three separate sets of 12 numbers each).      
    if game_mode == 3:
        # Prompt the player to choose one of the three dozen sections to bet on
        Dozen_bet = int(input('Vilken tredje del av bordet vill du spela på?\n'
                        'Del 1: 1-12\n'
                        'Del 2: 13-24\n'
                        'Del 3: 25-36\n\n'
                        'Skriv in siffran på den del du vill spela på, (1)(2)(3)\n'))

        # Prompt the player to specify the amount to bet on the chosen dozen
        Dozen_bet_size = int(input(f'Du har valt att spela på del {Dozen_bet}.\n'
                        f'Hur mycket vill du spela på del {Dozen_bet}?\nDu har {Balance} kvar att spela för.'))
        if not Check_balance(Dozen_bet_size): # Check if the player has enough balance to make the bet
            input(f'Du har inte {Dozen_bet_size} kvar att spela med. Du har {Balance} kvar att spela med\nTryck ENTER för att fortsätta') 
            continue                          # If not enough balance, continue to the next iteration to allow for another input
        
        # Map the user’s dozen choice to the actual numbers on the roulette wheel
        if Dozen_bet == 1:
            Dozen_bet = Dozen_bet_1           # Assign the first dozen numbers to Dozen_bet
        elif Dozen_bet == 2:
            Dozen_bet = Dozen_bet_2           # Assign the second dozen numbers to Dozen_bet
        elif Dozen_bet == 3:
            Dozen_bet = Dozen_bet_3           # Assign the third dozen numbers to Dozen_bet
        else:
            print("Invalid bet. Try again.")  # Notify the user of invalid input
            continue                          # Restart the loop to allow for correct input
        
                                            # Record the dozen bet with the chosen dozen and bet size
        all_bets['Dozen bet'].append({'dozen number': Dozen_bet, 'dozen bet size': Dozen_bet_size})


        Balance = Balance - Dozen_bet_size    # Deduct the bet amount from the player’s balance
# Option to place a bet on neighbours (a number and its two neighbours on the wheel).   
    if game_mode == 4:
        # Inform the player about the rules and mechanics of neighbor betting
        print('När du spelar grannar så delas din spelsumma jämnt på de nummret du väljer och dess grannar på roulett bordet')
        counter = 0
        for key, value in neighbours.items():   # Display all available numbers and their neighbors for betting 
            print(f"{key}, {value}", end="\t")  # use a tab for separation between pairs
            counter += 1
        
            if counter % 4 == 0:  # every 4 key-value pairs, move to the next line
                print()  # print a newline

        inre_loopa = True   # A flag to control the inner loop
        while inre_loopa:
            try:
                # Allow the player to choose a number for neighbor betting
                nr = int(input('\nViket nummer vill du spela grannar på...Tryck bara enter för att gå tbx till menyn\n'))

                the_neighbours = neighbours[nr]              # Retrieve the neighbors of the chosen number

                print(f'NR:{nr} har grannarna {the_neighbours}')

                neighbour_numbers = nr, the_neighbours[0],the_neighbours[1]

                # Allow the player to specify the bet size for the neighbor bet
                neighbour_bet_size = int(input(f'Hur mycket crediter vill du spela på nummer: {neighbour_numbers}\n'))
                if not Check_balance(neighbour_bet_size):    # Check if the player has enough balance to place the bet
                    input(f'Du har inte {neighbour_bet_size} kvar att spela med. Du har {Balance} kvar att spela med\nTryck ENTER för att fortsätta') 
                    continue
                Balance = Balance - neighbour_bet_size       # Deduct the bet amount from the player's balance
                
                bet_size_nr = neighbour_bet_size//3          # Deduct the bet amount from the player's balance
                
                print('Dina spel:')
                for nr in neighbour_numbers:

                    print(f'NR:{nr}---{bet_size_nr}kr')      # Show the player their placed bets
                                                            # Store the bet information in the all_bets dictionary
                    all_bets['neighbour bet'].append({'numbers': nr, 'neighbour number bet size': bet_size_nr})
            
                play_again=input('Har sparats!\nVill du spela på grannar igen?  Y/N: ')    # Confirm that the bets have been saved and ask the player if they want to place another bet
                
                if play_again == 'yes':
                    pass                                     # Keep the loop running if the player wants to place another bet
                else:
                    inre_loopa = False                       # Exit the loop if the player chooses not to place another bet
    
            except:
                inre_loopa = False                           # Handle any unexpected errors and exit the loop
        continue                                             # Takes the user back to the menu.
# Option to view all current bets.
    if game_mode == 5:
        Your_plays() # Calls on the Your_plays function.

        back_to_menu = input('\n\nTryck på ENTER för att gå tillbaka till menyn')
        continue     # Takes the user back to the menu.
# Option to repeat the last set of bets.
    if game_mode == 6:
        try:
            Same_play() # calls on the Same_play function.
        except:
            print('There are no previos bets to replicate')
# Option to roll the roulette wheel and see the result.
    if game_mode == 7:            
            # The game begins
            Your_plays()                    # Display the player's current bets
            Play()                          # Execute the Play function to simulate the roulette wheel spin and calculate the result
            total_bet = total_bet_size()    # Calculate the total bet amount of the player for this round

            last_betting_number = all_bets['Number bet'].copy()             # saving all plays yo new variabels so that i can re use them 
            last_betting_color = all_bets['Color bet']['color']             # if i want even after clearing the all_bets dict
            last_betting_color_size = all_bets['Color bet']['color bet size']
            last_betting_dozen = all_bets['Dozen bet'].copy() 
            last_betting_neighbour = all_bets['neighbour bet'].copy()

            if winnings > 0:  # Check if the player has won anything
                print(f'GRATTIS DU HAR VUNNIT {winnings}!\nDu gick +-({loss_profit})\n')
                time.sleep(2)
                print(f'Du har {Balance} kvar att spela med\n')

                time.sleep(1)
                svar = input('Tryck ENTER för att gå vidare')
                print('Du skickas vidare till menyn')
                Clear_Values()  # Clear all current bets after the round is over
                continue        # Continue to the next iteration of the game loop
            elif total_bet==0:
                print('Du hade inga spel denna runda!') # Notify the player if no bets were placed
                time.sleep(1)
            else:              # else (om vinst inte är mer än 0) kolla om spelarens saldo är mer än 0 annars är spelet slut
                if Balance >0:
                    print(f'Tyvärr, du missa denna gång. Du gick {loss_profit}\nDu har {Balance} kvar att spela med\n')
                
                    time.sleep(1)
                    svar = input('Tryck ENTER för att gå vidare')
                    Clear_Values()  # Clear all current bets after the round is over
                    continue  # Continue to the next iteration of the game loop
                else:
                    print('Tyvärr du är nollad. Bättre lycka nästa gång')    # Notify the player if the balance is zero
                    break   # Exit the game loop as the player can't place more bets