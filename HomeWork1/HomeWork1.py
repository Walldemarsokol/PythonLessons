# Задача 6. Напишите программу, которая принимает на вход цифру обозначающую день недели и проверяет является ли этото день выходным

# n=(int(input('Введите цифру от 1 до 7:  ')))
# print('No' if n>0 and n<6 else 'Yes')

#Задача 7.

#Задача 8.

# x =int(input('Введите значение Х : '))
# y =int(input('Введите значение У : '))

# if x>0 and y>0: #or (x<0 and y>0) or (x<0 and y<0) or (x>0 and y<0):
#     print('1')
# elif x<0 and y>0:
#     print('2')
# elif x<0 and y<0:
#     print('3')
# else:
#     print('4')

#Задача 9.
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

import math

x1= int(input('Введите координаты x1: '))
y1= int(input('Введите координаты y1: '))
x2= int(input('Введите координаты x2: '))
y2= int(input('Введите координаты y2: '))
result = float(math.sqrt((x2-x1)**2+(y2-y1)**2))
print(f'{result:.2f}')
