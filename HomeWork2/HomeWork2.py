#Задача 14.Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.

# n = input('Введите число: ')
# if ',' or '.' in n:
#     n = n.replace(',', '')
#     n = n.replace('.', '')
#     A = 1
# result = []
# res = 0
# for i in range(0, len(n), A):
#     result.append(int(n[i: i + A]))

# for j in range(0, len(result)):
#     res = res + result[j]
# else:
#     A = 1
# result = []
# res = 0
# for i in range(0, len(n), A):
#     result.append(int(n[i: i + A]))

# for j in range(0, len(result)):
#     res = res + result[j]

# print(f'Сумма цифр равна:{res}')

#Задача 15. Напишите программу, которая принимает на 
# вход число N и выдает набор произведений чисел от 1 до N.

# n=int(input('Введите число: '))
# i=1
# j=0
# res=1
# some_list=[n]
# some_list2=[n]
# while i<=n and j<n:
#     res=res*i
#     i=i+1
#     some_list.insert (j, res)
#     j=j+1
#     print(res)
# print(some_list[:-1],some_list2)

# Задача 16.Задайте список из 
# n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# import math

# n=int(input())
# sum=0
# print('{',end='')
# for i in range(1,n):
#     sum=sum+ round(((1+1/i)**i),2)
#     print(f'{i}:{round(((1+1/i)**i),2)}',end=',')
# print(f'{n}:{round(((1+1/n)**n),2)}',end='}')
# print(f'\n Сумма чисел равна: {sum+round(((1+1/n)**n),2)} \n')

#Задача 18. Реализуйте алгоритм перемешивания списка.

# from random import randint
# import random

# n=randint(3,6)

# list=[n]
# for i in range(n):
#     list.append(randint(10,50))
# print(list)

# random.shuffle(list)
# print(list)