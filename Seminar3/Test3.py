
# number = float(input())
# summ = 0
# while number != 0:
#     summ += number % 10
# number //= 10
# print(summ)

#Задача.Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import *

# n=int(input('Введите число: '))
# some_list=[]
# for _ in range(n):
#     some_list.append(randint(-n,n))
# print(some_list)
# with open('file2.txt', 'w', encoding='utf-8') as f:#строка создает файл file2.txt и элемент 'w' дает команду записи в файл
#     for _ in range(randint(1,n)):#задает количетсво индексов для умножения
#         f.write(str(randint(0,n-1))+'\n')#задает номера индексов
# fact=1
# with open('file2.txt', 'r', encoding='utf-8') as f:#строка читает файл
#     f=f.read().splitlines()
#     for number in f:
#         fact*=some_list[int(number)]# производит умножение значений индексов друг на друга
# print(fact)


# #реализуйте алгоритм перемешивания списка
# some_list=[1,4,5,10]
# for _ in range(random.randint(1,10)):
#     i1=random.randint(0,len(some_list)-1)
#     i2=random.randint(0,len(some_list)-1)
#     some_list[i1],some_list[i2]=some_list[i2],some_list[i1]
# print(some_list)