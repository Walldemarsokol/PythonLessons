# Задача 6. Напишите программу, которая принимает на вход цифру обозначающую день недели и проверяет является ли этото день выходным

# n=(int(input('Введите цифру от 1 до 7:  ')))
# print('No' if n>0 and n<6 else 'Yes')

#Задача 7.
# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. not(x or y or z) = not x and not y and not z

# def input_numbers():
#     for x in range(0,2):
#         for y in range(0,2):
#             for z in range(0,2):
#                 left_part = not (x or y or z)
#                 rigth_part = not x and not y and not z
#                 if left_part == rigth_part:
#                     print("Утверждение истинно")
#                 else:
#                     print('Утверждение ложно')
# print(input_numbers())

#Задача 8.
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# x =int(input('Введите значение Х : '))
# y =int(input('Введите значение У : '))
# if x==0 and y==0:
#     print('Введите другое значение Х и У')
# else:
#     if x>0 and y>0: #or (x<0 and y>0) or (x<0 and y<0) or (x>0 and y<0):
#         print('1')
#     elif x<0 and y>0:
#         print('2')
#     elif x<0 and y<0:
#         print('3')
#     else:
#         print('4')

#Задача 9.
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# x =int(input('Введите номер четверти от 1 до 4 : '))

# if x==1: #or (x<0 and y>0) or (x<0 and y<0) or (x>0 and y<0):
#     print('Диапазон возможных координат: x>0 and y>0')
# elif x==2:
#     print('Диапазон возможных координат: x<0 and y>0')
# elif x==3:
#     print('Диапазон возможных координат: x<0 and y<0')
# else:
#     print('Диапазон возможных координат: x>0 and y<0')

#Задача 10.
# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# import math

# x1= int(input('Введите координаты x1: '))
# y1= int(input('Введите координаты y1: '))
# x2= int(input('Введите координаты x2: '))
# y2= int(input('Введите координаты y2: '))

# print(f'{float(math.sqrt((x2-x1)**2+(y2-y1)**2)):.2f}')
