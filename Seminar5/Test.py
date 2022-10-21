# indexes_degree = { "0": "\u2070",
#                    "1": "\u00B9",
#                    "2": "\u00B2",
#                    "3": "\u00B3",
#                    "4": "\u2074",
#                    "5": "\u2075",
#                    "6": "\u2076",
#                    "7": "\u2077",
#                    "8": "\u2078",
#                    "9": "\u2079",
#                    "-": "\u207B"
#            }

# def super_symbol(n): # преобразует число в надстрочный символ для записи в файл
#     n = str(n)
#     result = ''
#     for i in range(len(n)):
#         if int(str(n)[i]) == 1:
#             result += str(chr(0x00b9))
#         elif 1 < int(str(n)[i]) <= 3:
#             result += str(chr(0x00b0 + int(str(n)[i])))
#         else:
#             result += str(chr(0x2070 + int(str(n)[i])))


# from random import randint
# import random

# k = int(input('Введите натуральную степень k: '))
# while k <= 0:
#     k = int(input('Введены не корректные данные! Введите натуральную степень k: '))

# result = [0 for i in range(k)]
# koef = random.sample(range(0, 101), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
# print(f'До обработки: {result}')
# for elem in result:
#     if elem == 0:
#         result.remove(elem)
#     try:
#         ind_x = elem.find('x')
#         d = int(elem[:ind_x])
#     except AttributeError:
#         continue
#     if d == 0 or elem == '0':
#         result.remove(elem)
#     if '^1' in elem:
#         result.remove(elem)
#         result.insert(-1, elem[:elem.find('^1')])
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result) - 1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)

# with open('text.txt', 'w') as f:
#     f.write(polynom)


# a = [3, 2, 2, 3, 4, 1, 4, 0, 3, 4, 5, 2, 5, 5]
# b = set(a)
# b = list(b)
# print(a)
# print(b)

# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# from random import randint


# def create_file():
#     with open('data/task01.txt', 'w', encoding='utf-8') as file:
#         rand_num = randint(2, 14)
#         for i in range(1, 15 + 1):
#             if i != rand_num:
#                 file.write(str(i) + ' ')


# def find_number():
#     with open('data/task01.txt', 'r', encoding='utf-8') as file:
#         list_nums = file.read()
#         list_nums = list(map(int, list_nums.split()))
#         print(list_nums)
#         for i in range(1, len(list_nums)):
#             if (list_nums[i] - 1) != list_nums[i - 1]:
#                 print(list_nums[i] - 1)


# create_file()
# find_number()

# another 
# n = 8
# with open('coef.txt', 'r', encoding='utf-8') as k:
#     some_list = list(map(int, k.read().split()))
#     for i in range(n - 1):
#         if some_list[i] != some_list[i + 1] - 1:
#             print(some_list[i + 1] - 1)



# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# text = input()
# text = text.split()
# new_text = list(filter(lambda i: 'abc' not in i, text))
# print(new_text)




# Дан список интов повторяющихся элементов в списке нет. 
# Нужно преобразовать это множество в строку сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

# int_list = [0, 1, 2, 3, 4, 5, 8, 9, 11]
# int_list.sort()
# idx = 0
# new_list = []
# while idx < len(int_list):
#     some_list = [int_list[idx]]
#     new_idx = idx
#     while new_idx + 1 != len(int_list) and int_list[new_idx] == int_list[new_idx + 1] - 1:
#         some_list.append(int_list[new_idx + 1])
#         new_idx += 1
#     new_list.append(some_list)
#     idx += len(some_list)
# print(new_list)
# a = []
# for i in new_list:
#     if len(i) != 1:
#         a.append(f'{i[0]}-{i[-1]}')
#     else:
#         a.append(f'{i[0]}')
# print(*a, sep=',')


#another
# def border_val(lst_int):
#     lst_int = sorted(lst_int)
#     ans = [[lst_int[0]]]

#     for ind in range(0, len(lst_int) - 1):
#         if (ind == len(lst_int) - 2) and (lst_int[ind + 1] == lst_int[ind] + 1):
#             ans[-1].append(lst_int[ind + 1])
#         if lst_int[ind + 1] != lst_int[ind] + 1:
#             ans[-1].append(lst_int[ind])
#             ans.append([lst_int[ind + 1]])

#     for i in range(len(ans)):
#         if max(ans[i]) != min(ans[i]):
#             ans[i] = f'{min(ans[i])}-{max(ans[i])}'
#         else:
#             ans[i] = f'{min(ans[i])}'

#     print(', '.join(ans))
