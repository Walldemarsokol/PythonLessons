# #задача 2 из дз.
# count = int(input('Введите колиество элементов: '))
# some_list = []
# for _ in range( count):
#     number = int(input())
#     some_list.append(number)

# new_list = []
# for idx in range((count-1)//2+1):
#     number1=some_list[idx]
#     number2=some_list[count-idx -1]
#     new_list.append(number1*number2)
# print(new_list)

#Задача 27.Задайте строку из набора чисел. Напишите программу, 
# которая выводит большее и меньшее число. В качестве разделителя 
# испольуйте пробел

# n=list(map(int,input('Enter numbers: ').split()))
# maxx=max(n)
# minn=min(n)
# print(f'max={maxx},min={minn}')

#Задача 28. Найдите корни квадратного уравнения Ах2+Вх+С=0 двумя способами:
#a)через математич формулы
#b)через функции пайтон
# a)
# import math
# a=int(input())
# b=int(input())
# c=int(input())
# d=(b*b)-4*a*c
# if d<0:
#     print('No answer')
# if d==0:
#     print((-b)/(2*a))
# if d>0:
#     print(round(((-b)+math.sqrt(d))/(2*a),2))
#     print(round(((-b)-math.sqrt(d))/(2*a),2))

# b)
# from sympy import discriminant
# from sympy.abc import x

# a=int(input())
# b=int(input())
# c=int(input())

# print(discriminant(a*(x**2)+b*x+c))
#Задача 29. Напишите программу, 
# которая найдет наименьшее общее кратное двух чисел.





