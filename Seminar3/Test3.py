
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


# # #реализуйте алгоритм перемешивания списка
# from random import *
# import time

# #a=3  b=7  (time.time  берем правую часть после точки )%(b-a+1)+a

# now=time.time() #покажет число секунд и милисекунд с начала эпохи
# random_number = str(time.time()).split('.')[1] #преобрахуем в строчки, жадим на две части от точки и берем левую от точки
# print(random_number)
# # some_list=[1,4,5,10]
# # for _ in range(random.randint(1,10)):
# #     i1=random.randint(0,len(some_list)-1)
# #     i2=random.randint(0,len(some_list)-1)
# #     some_list[i1],some_list[i2]=some_list[i2],some_list[i1]
# # print(some_list)

# some_list=[1,4,5,10]
# for _ in range(int(str(time.time()).split('.')[1])%(10-5+1)+5):
#     i1=int(str(time.time()).split('.')[1])%(4-0)+0
#     time.sleep(0.00001) #функция дает программе паузу.в данном случае для правильной работы
#     i2=int(str(time.time()).split('.')[1])%(4-0)+0
#     some_list[i1],some_list[i2]=some_list[i2],some_list[i1]
# print(some_list)

#Функции 
# def hello(name:str):
#     print('hello',name)

# hello('Alex')

# def hello(name='незнакомец'):#если в функции уже есть какой-то параметр и если не вводить 
#                             #новый при вызове функции, то будет выводиться аргумент по умолчанию из функции
#     print('hello',name)

# hello()# hello незнакомец

# def mult(a=1, b=1):
#     return a*b

# m = mult(5,10)
# print(m)
# def add(m,n):
#     return m+n

# def mult(a=1, b=1):
#     print(a*b)

# mult(add(5,10), add(10,20))


#Задача 19. Реализуйте алгоритм генератора случайных чисел 
# без использования встроенного генератора псевдослучайных чисел

# import time
# print(time.time())

#Задача20.Задайте список.Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.

# a=[input() for _ in range(int(input()))] #эта строчка заменяет количество других строк, а именно:
# # a=[]
# # n=int(input())
# # for _ in range(n):
# #     a.append(input())
# find_number = input('Введите искомое число: ')
# if find_number in a:
#     print('да')
# else:
#     print('нет')
# a=[]
# n=int(input())
# for _ in range(n):
#     a.append(input())
# find_number = input('Введите искомое число: ')
# for i in a: #если нам нужно пробежаться по значению строки из нескольких елементов, то подойдет такое решение
#     if find_number in i:
#         print('yes')
#         break
#     else:
#         print('no')

#Задача21.Напишите программу, которая определит позицию в списке второго вхождения строки в списке 
# либо сообщит, что ее нет
# a=[]
# n=int(input())
# for _ in range(n):
#     a.append(input())
# find_str = input('Введите искомое значение ')
# count=0
# for el in range(len(a)):
#     if a[el] == find_str:
#         count+=1
#     if count==2:
#         print(el)
#         break
# else:
#     print('-1')

# a=[]
# n=int(input())
# for _ in range(n):
#     a.append(input())
# find_str = input('Введите искомое значение ')
# first=a.index(find_str)#у функции индекс есть условие поиска с определенного элемента,
# #его мы и укажем во втором вхождении после нахождения первого индекса
# second = a.index(find_str,first +1 )
# print(second)