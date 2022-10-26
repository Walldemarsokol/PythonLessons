#Создайте программу для игры с конфетами человек против человека.
print('\n"Welcome to the candy-game! Lets start!"\n')
total_sweets=2021
player_2nd_have=0
player_1st_have=0
while total_sweets>0:
    turn_1_player=int(input('1st player turn. Enter number limit in 1-28: '))# enter 
    if turn_1_player>0 and turn_1_player<29:
        print(f'Left{total_sweets}')  # how many sweets we are have
        total_sweets=total_sweets-turn_1_player  # turn 1st player
        player_1st_have=player_1st_have+turn_1_player   #1st player have sweets
        print(f'1st Player have a {player_1st_have} candy`s')
        if total_sweets==0:
            print('Congratilations!1st Player win!')
    else:
        print('Enter another number: ')
    
    
    turn_2_player=int(input('2st player turn. Enter number limit in 1-28: '))
    if turn_2_player>0 and turn_2_player<29:
        print(f'Left{total_sweets}')
        total_sweets=total_sweets-turn_2_player
        player_2nd_have=player_2nd_have+turn_2_player
        print(f'2nd Player have a {player_2nd_have} candy`s')
        if total_sweets==0:
            print('Congratilations!1st Player win!')
    else:
        print('Enter another number: ')
    
