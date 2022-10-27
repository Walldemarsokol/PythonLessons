
# Создайте программу для игры с конфетами человек против человека.
import random
import time


def check_number(x, y, z):
    x = str(x)
    if x.isnumeric() is True:
        x = int(x)
        if x == y:
            return x
        if x == z:
            return x
        if x >= y and x <= z:
            return x
        else:
            return check_number(input('Enter correct number: '), y, z)
    else:
        return check_number(input('Enter correct number: '), y, z)


print('\n"Welcome to the candy-game! Lets start!"\n')
print('____________________________________________ \n')
mode = int(input('Choose your game mode: PvP(enter 1) or PvEasyBot (enter 2) or PvSmartBot (enter 3)'))
mode = check_number(mode, 1, 3)
total_sweets = int(input('Choose how many sweets will be in game:')) #Choose 2021 if is a homework
player_2nd_have = 0
player_1st_have = 0
if mode == 1:
    name_1 = str(input('Enter 1st Player name: '))
    name_2 = str(input('Enter 2nd Player name: '))
    while total_sweets > 0:
        print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have

        if total_sweets <= 28:
            turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
            turn_1_player = check_number(turn_1_player, 1, total_sweets)
            total_sweets = total_sweets-turn_1_player
            player_1st_have += turn_1_player
            print('____________\n')
            if total_sweets == 0:
                player_1st_have = player_2nd_have+player_1st_have
                print(f'{name_1} have all {player_1st_have} candy`s. ')
                print(f'Congratilations! {name_1} win!')
                time.sleep(5)
                break
        else:
            turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')  # enter number
            turn_1_player = check_number(turn_1_player, 1, 28)
            total_sweets = total_sweets-turn_1_player  # turn 1st player
            player_1st_have += turn_1_player  # 1st player have sweets
            print(f'{name_1} have a {player_1st_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')

        print(f'Left {total_sweets} sweets in basket')
        if total_sweets <= 28:
            turn_2_player = input(f'Now is {name_2} turn. Enter number limit in 1-28: ')
            turn_2_player = check_number(turn_2_player, 1, total_sweets)
            total_sweets = total_sweets-turn_2_player
            player_2nd_have += turn_2_player
            print('____________\n')
            if total_sweets == 0:
                player_2nd_have = player_2nd_have+player_1st_have
                print(f'{name_2} have all {player_2nd_have} candy`s. ')
                print(f'Congratilations! {name_2} win!')
                time.sleep(5)
                break
        else:
            turn_2_player = input(f'Now is {name_2} turn. Enter number limit in 1-28: ')
            turn_2_player = check_number(turn_2_player, 1, 28)
            total_sweets = total_sweets-turn_2_player
            player_2nd_have += turn_2_player
            print(f'{name_2} have a {player_2nd_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')


if mode == 2:
    name_1 = str(input('Enter 1st Player name: \n'))
    while total_sweets > 0:
        print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have

        if total_sweets <= 28:
            turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
            turn_1_player = check_number(turn_1_player, 1, total_sweets)
            total_sweets = total_sweets-turn_1_player
            player_1st_have += turn_1_player
            print('____________\n')
            if total_sweets == 0:
                player_1st_have = player_2nd_have+player_1st_have
                print(f'{name_1} have all {player_1st_have} candy`s. ')
                print('Congratilations! 1st Player win!')
                time.sleep(5)
                break
        else:
            turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')  # enter
            turn_1_player = check_number(turn_1_player, 1, 28)
            total_sweets = total_sweets-turn_1_player  # turn 1st player
            player_1st_have += turn_1_player  # 1st player have sweets
            print(f'{name_1} have a {player_1st_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')

        print(f'Left {total_sweets} sweets in basket')
        if total_sweets <= 28:
            turn_2_player = random.randint(1, total_sweets)
            print(f'Now is EasyBot turn. Enter number {turn_2_player}')
            total_sweets = total_sweets-turn_2_player
            player_2nd_have += turn_2_player
            print('____________\n')
            if total_sweets == 0:
                player_2nd_have = player_2nd_have+player_1st_have
                print(f'EasyBot have all {player_2nd_have} candy`s. ')
                print('Congratilations! EasyBot win!')
                time.sleep(5)
                break
        else:
            turn_2_player = random.randint(1, 28)
            print(f'Now is EasyBot. Enter number {turn_2_player}')
            total_sweets = total_sweets-turn_2_player
            player_2nd_have += turn_2_player
            print(f'EasyBot have a {player_2nd_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')

if mode == 3:
    name_1 = str(input('Enter 1st Player name: \n'))
    while total_sweets > 0:
        print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have
        
        if total_sweets<=28:
            turn_1_player =input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
            turn_1_player =check_number(turn_1_player,1,total_sweets)
            total_sweets = total_sweets-turn_1_player
            player_1st_have+=turn_1_player
            print('____________\n')
            if total_sweets == 0:
                player_1st_have=player_2nd_have+player_1st_have
                print(f'{name_1} have all {player_1st_have} candy`s. ')
                print('Congratilations! 1st Player win!')
                time.sleep(5)
                break
        else:                    
            turn_1_player =input(f'Now is {name_1} turn. Enter number limit in 1-28: ')# enter
            turn_1_player=check_number(turn_1_player,1,28)
            total_sweets = total_sweets-turn_1_player  # turn 1st player
            player_1st_have+=turn_1_player  # 1st player have sweets
            print(f'{name_1} have a {player_1st_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')
        
        print(f'Left {total_sweets} sweets in basket')
        if total_sweets<=28:
            turn_2_player = total_sweets
            print(f'Now is SmartBot turn. Enter number {turn_2_player}')
            total_sweets = total_sweets-turn_2_player
            player_2nd_have+=turn_2_player
            print('____________\n')
            if total_sweets == 0:
                player_2nd_have=player_2nd_have+player_1st_have
                print(f'SmartBot have all {player_2nd_have} candy`s. ')
                print('Congratilations! EasyBot win!')
                time.sleep(5)
                break
        else:        
            turn_2_player = 28
            print(f'Now is SmartBot. Enter number {turn_2_player}')
            total_sweets = total_sweets-turn_2_player
            player_2nd_have+=turn_2_player
            print(f'SmartBot have a {player_2nd_have} candy`s')
            print(f'Left {total_sweets} sweets in basket')
            print('____________\n')
