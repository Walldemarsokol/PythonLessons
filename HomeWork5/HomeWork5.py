# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# some_list=list(input().split())
# print(some_list)
# new_list=[]
# find='abc'
# for i in range(len(some_list)):
#     if find not in some_list[i]:
#         new_list.append(some_list[i])

# print(new_list)

#второй вариант из семинара:

# text = input()
# text = text.split()
# new_text = list(filter(lambda i: 'abc' not in i, text))
# print(new_text)




# # Создайте программу для игры с конфетами человек против человека.
# import random
# import time


# def check_number(x, y, z):
#     x = str(x)
#     if x.isnumeric() == True:
#         x = int(x)
#         if x == y:
#             return x
#         if x == z:
#             return x
#         if x >= y and x <= z:
#             return x
#         else:
#             return check_number(input('Enter correct number: '), y, z)
#     else:
#         return check_number(input('Enter correct number: '), y, z)


# print('\n"Welcome to the candy-game! Lets start!"\n')
# print('____________________________________________ \n')
# mode = int(input('Choose your game mode: PvP(enter 1) or PvEasyBot (enter 2) or PvSmartBot (enter 3)'))
# mode = check_number(mode, 1, 3)
# total_sweets = int(input('Choose how many sweets will be in game:')) #Choose 2021 if is a homework
# player_2nd_have = 0
# player_1st_have = 0
# if mode == 1:
#     name_1 = str(input('Enter 1st Player name: '))
#     name_2 = str(input('Enter 2nd Player name: '))
#     while total_sweets > 0:
#         print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have

#         if total_sweets <= 28:
#             turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
#             turn_1_player = check_number(turn_1_player, 1, total_sweets)
#             total_sweets = total_sweets-turn_1_player
#             player_1st_have += turn_1_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_1st_have = player_2nd_have+player_1st_have
#                 print(f'{name_1} have all {player_1st_have} candy`s. ')
#                 print(f'Congratilations! {name_1} win!')
#                 time.sleep(5)
#                 break
#         else:
#             turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')  # enter number
#             turn_1_player = check_number(turn_1_player, 1, 28)
#             total_sweets = total_sweets-turn_1_player  # turn 1st player
#             player_1st_have += turn_1_player  # 1st player have sweets
#             print(f'{name_1} have a {player_1st_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')

#         print(f'Left {total_sweets} sweets in basket')
#         if total_sweets <= 28:
#             turn_2_player = input(f'Now is {name_2} turn. Enter number limit in 1-28: ')
#             turn_2_player = check_number(turn_2_player, 1, total_sweets)
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have += turn_2_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_2nd_have = player_2nd_have+player_1st_have
#                 print(f'{name_2} have all {player_2nd_have} candy`s. ')
#                 print(f'Congratilations! {name_2} win!')
#                 time.sleep(5)
#                 break
#         else:
#             turn_2_player = input(f'Now is {name_2} turn. Enter number limit in 1-28: ')
#             turn_2_player = check_number(turn_2_player, 1, 28)
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have += turn_2_player
#             print(f'{name_2} have a {player_2nd_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')


# if mode == 2:
#     name_1 = str(input('Enter 1st Player name: \n'))
#     while total_sweets > 0:
#         print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have

#         if total_sweets <= 28:
#             turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
#             turn_1_player = check_number(turn_1_player, 1, total_sweets)
#             total_sweets = total_sweets-turn_1_player
#             player_1st_have += turn_1_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_1st_have = player_2nd_have+player_1st_have
#                 print(f'{name_1} have all {player_1st_have} candy`s. ')
#                 print('Congratilations! 1st Player win!')
#                 time.sleep(5)
#                 break
#         else:
#             turn_1_player = input(f'Now is {name_1} turn. Enter number limit in 1-28: ')  # enter
#             turn_1_player = check_number(turn_1_player, 1, 28)
#             total_sweets = total_sweets-turn_1_player  # turn 1st player
#             player_1st_have += turn_1_player  # 1st player have sweets
#             print(f'{name_1} have a {player_1st_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')

#         print(f'Left {total_sweets} sweets in basket')
#         if total_sweets <= 28:
#             turn_2_player = random.randint(1, total_sweets)
#             print(f'Now is EasyBot turn. Enter number {turn_2_player}')
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have += turn_2_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_2nd_have = player_2nd_have+player_1st_have
#                 print(f'EasyBot have all {player_2nd_have} candy`s. ')
#                 print('Congratilations! EasyBot win!')
#                 time.sleep(5)
#                 break
#         else:
#             turn_2_player = random.randint(1, 28)
#             print(f'Now is EasyBot. Enter number {turn_2_player}')
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have += turn_2_player
#             print(f'EasyBot have a {player_2nd_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')

# if mode == 3:
#     name_1 = str(input('Enter 1st Player name: \n'))
#     while total_sweets > 0:
#         print(f'Left {total_sweets} sweets in basket')  # how many sweets we are have
        
#         if total_sweets<=28:
#             turn_1_player =input(f'Now is {name_1} turn. Enter number limit in 1-28: ')
#             turn_1_player =check_number(turn_1_player,1,total_sweets)
#             total_sweets = total_sweets-turn_1_player
#             player_1st_have+=turn_1_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_1st_have=player_2nd_have+player_1st_have
#                 print(f'{name_1} have all {player_1st_have} candy`s. ')
#                 print('Congratilations! 1st Player win!')
#                 time.sleep(5)
#                 break
#         else:                    
#             turn_1_player =input(f'Now is {name_1} turn. Enter number limit in 1-28: ')# enter
#             turn_1_player=check_number(turn_1_player,1,28)
#             total_sweets = total_sweets-turn_1_player  # turn 1st player
#             player_1st_have+=turn_1_player  # 1st player have sweets
#             print(f'{name_1} have a {player_1st_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')
        
#         print(f'Left {total_sweets} sweets in basket')
#         if total_sweets<=28:
#             turn_2_player = total_sweets
#             print(f'Now is SmartBot turn. Enter number {turn_2_player}')
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have+=turn_2_player
#             print('____________\n')
#             if total_sweets == 0:
#                 player_2nd_have=player_2nd_have+player_1st_have
#                 print(f'SmartBot have all {player_2nd_have} candy`s. ')
#                 print('Congratilations! EasyBot win!')
#                 time.sleep(5)
#                 break
#         else:        
#             turn_2_player = 28
#             print(f'Now is SmartBot. Enter number {turn_2_player}')
#             total_sweets = total_sweets-turn_2_player
#             player_2nd_have+=turn_2_player
#             print(f'SmartBot have a {player_2nd_have} candy`s')
#             print(f'Left {total_sweets} sweets in basket')
#             print('____________\n')

#_____________________________
#Задача 42.Создайте RLE алгоритм. реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def encode(s):
    encoding = "" # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

def uncode(s):
    uncoding =str # сохраняет выходную строку
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        for a in range(len(s)):
            if a%2==0:
                r=int(s[a])
                while r>0:
                    uncoding
                    r-=1
            else:
                uncoding+=s[a]
    return uncoding

some_list=''
with open('file.txt', 'r', encoding='utf-8') as f:# read text in file
    f=f.read()
    some_list=f
some_list=encode(some_list)
with open('file1.txt','w',encoding='utf-8') as f:# write new coding to file
    f.write(some_list)
with open('file1.txt', 'r', encoding='utf-8') as f:# read text in file1
    f=f.read()
    some_list=f
print(uncode(some_list))
# with open('file2.txt', 'r',encoding='utf-8') as f:
#     f=f.write(some_list)