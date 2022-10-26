#Создайте программу для игры с конфетами человек против человека.
import time 
def check_number(x,y,z):
    x=str(x)
    if x.isnumeric()==True:
        x=int(x)
        if x==y:
            return x
        if x==z:
            return z
        if x>y and x<=z:
            return x
        else:
            return check_number(input('Enter correct number: '),y,z)
    else:
        return check_number(input('Enter correct number: '),y,z)

print('\n"Welcome to the candy-game! Lets start!"\n')
print('____________________________________________ \n')
mode=(int(input('Choose game mode: PvP(enter 1) or PvBot (enter 2)')))
mode=check_number(mode,1,2)
total_sweets = 100
player_2nd_have = 0
player_1st_have = 0
if mode == 1:
    while total_sweets > 0:
        print(f'Left {total_sweets} in basket')  # how many sweets we are have
        
        if total_sweets<=28:
            turn_1_player =input('1st player turn. Enter number limit in 1-28: ')
            turn_1_player =check_number(turn_1_player,1,total_sweets)
            total_sweets = total_sweets-turn_1_player
            player_1st_have+=turn_1_player
            print('____________\n')
            if total_sweets == 0:
                player_1st_have=player_2nd_have+player_1st_have
                print(f'Player2 have all {player_2nd_have} candy`s. ')
                print('Congratilations! 1st Player win!')
                time.sleep(5)
                break
                               
        turn_1_player =input('1st player turn. Enter number limit in 1-28: ')# enter
        turn_1_player=check_number(turn_1_player,1,28)
        total_sweets = total_sweets-turn_1_player  # turn 1st player
        player_1st_have+=turn_1_player  # 1st player have sweets
        print(f'1st Player have a {player_1st_have} candy`s')
        print(f'Left {total_sweets} in basket')
        print('____________\n')
        
        print(f'Left {total_sweets} in basket')
        if total_sweets<=28:
            turn_2_player =input('1st player turn. Enter number limit in 1-28: ')
            turn_2_player =check_number(turn_2_player,1,total_sweets)
            total_sweets = total_sweets-turn_2_player
            player_2nd_have+=turn_2_player
            print('____________\n')
            if total_sweets == 0:
                player_2nd_have=player_2nd_have+player_1st_have
                print(f'Player2 have all {player_2nd_have} candy`s. ')
                print('Congratilations! 2st Player win!')
                time.sleep(5)
                break
                
        turn_2_player =input('2st player turn. Enter number limit in 1-28: ')
        turn_2_player =check_number(turn_2_player,1,28)
        total_sweets = total_sweets-turn_2_player
        player_2nd_have+=turn_2_player
        print(f'2nd Player have a {player_2nd_have} candy`s')
        print(f'Left {total_sweets} in basket')
        print('____________\n')


if mode==2:
    while total_sweets > 0:
        print(f'Left {total_sweets} in basket')  # how many sweets we are have
        
        if total_sweets<=28:
            turn_1_player =input('1st player turn. Enter number limit in 1-28: ')
            turn_1_player =check_number(turn_1_player,1,total_sweets)
            total_sweets = total_sweets-turn_1_player
            player_1st_have+=turn_1_player
            print('____________\n')
            if total_sweets == 0:
                player_1st_have=player_2nd_have+player_1st_have
                print(f'Player2 have all {player_2nd_have} candy`s. ')
                print('Congratilations! 1st Player win!')
                time.sleep(5)
                break
                               
        turn_1_player =input('1st player turn. Enter number limit in 1-28: ')# enter
        turn_1_player=check_number(turn_1_player,1,28)
        total_sweets = total_sweets-turn_1_player  # turn 1st player
        player_1st_have+=turn_1_player  # 1st player have sweets
        print(f'1st Player have a {player_1st_have} candy`s')
        print(f'Left {total_sweets} in basket')
        print('____________\n')
        
        print(f'Left {total_sweets} in basket')
        if total_sweets<=28:
            turn_2_player =input('1st player turn. Enter number limit in 1-28: ')
            turn_2_player =check_number(turn_2_player,1,total_sweets)
            total_sweets = total_sweets-turn_2_player
            player_2nd_have+=turn_2_player
            print('____________\n')
            if total_sweets == 0:
                player_2nd_have=player_2nd_have+player_1st_have
                print(f'Player2 have all {player_2nd_have} candy`s. ')
                print('Congratilations! 2st Player win!')
                time.sleep(5)
                break
                
        turn_2_player =input('2st player turn. Enter number limit in 1-28: ')
        turn_2_player =check_number(turn_2_player,1,28)
        total_sweets = total_sweets-turn_2_player
        player_2nd_have+=turn_2_player
        print(f'2nd Player have a {player_2nd_have} candy`s')
        print(f'Left {total_sweets} in basket')
        print('____________\n')