
import random
correct_number = 7
guess_limit = 3
player_count = 0

start_menu = input("\033[96mSELECT:\nplay\nhelp\nexit\n")
if start_menu == 'play':
    print('\033[92mWelcome to the game!')
    while guess_limit > player_count:
        guess = int(input('pick a number 1-10 ->'))
        if guess < correct_number:
            print('Number too low!')
        elif guess > correct_number:
            print('Number too high!')
        elif guess == correct_number:
            print('congratulations you won !')
            break
        player_count += 1

        if player_count == guess_limit:
            print(f'\033[92m sorry you lose the correct number was {correct_number}')

elif start_menu == 'help':
    print("\033[95m player must must pick a number\nfrom a set range. The player gets three guesses")
elif start_menu == 'exit':
    print('Until next time!')
else:
    print("\033[91mI'm sorry an error has occurred please try again")







