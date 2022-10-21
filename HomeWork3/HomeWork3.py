#Задача 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# list=input('введите числа через пробел: ')
# list =list.replace(' ','')
# sum=0
# for i in range(0,len(list)):
#     if i%2!=0:
#         n=int(list[i])
#         sum= sum+n
# print(f'Answer: {sum}')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# list_of_product =[]
# n=int(input("Введите размер списка: "))
# list=[]
# for i in range(n):
#     list.append(int(input('введите числа через enter: ')))
# if  n%2==0:
#     x=n-1
#     z=int(n/2)
#     a=0
#     while a<n/2:
#         for j in range(z):
#             list_of_product.append(list[j]*list[x])
#             # print(list[j])
#             x-=1
#             a+=1
# if n%2!=0:
#     x=n-1
#     z=int(n//2+1)
#     a=0
#     while a<n//2+1:
#         for j in range(z):
#             list_of_product.append(list[j]*list[x])
#             # print(list[j])
#             x-=1
#             a+=1

# print(list)
# print(list_of_product)

# Задача 3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# some_list=[]
# another_list=[]
# for n in range(3):
#     some_list.append(input(f'введите число {n+1} через enter: '))
#     i=float(some_list[n])
#     x=round((i%1),2)
#     another_list.append(x)
# max_n=max(another_list)
# min_n=min(another_list)
# print(f"{max_n-min_n}")


#Задача4. Напишите программу, которая
# будет преобразовывать десятичное число в двоичное.

# n=int(input())
# m=n
# p=1
# d1=0
# while m>0:
#     d1=d1+m%2*p
#     p=p*10
#     m=m//2
# print(d1)

# a=int(input())
# b=''
# while a!=0:
#     b=str(a%2)+b
#     a//=2
# print(b)
#или еще вариант с использованием синтаксиса
# print(bin(int(input())))

#Задача про негафибоначчи

# k = int(input())
# # строка позволит создать определенное количество элементовы в списке
# some_list = [0]*(k*2+1)
# some_list[k+1] = 1
# for idx in range(k+2,k*2+1):
#     some_list[idx]=some_list[idx-1]+ some_list[idx-2]

# for idx in range(k,-1,-1): #идем в лево до нулевого, но т.к. нулевой не вклчается, то пишем до -1, шаг хода в лево -1
#     some_list[idx]= some_list[idx+2]-some_list[idx+1]
# print(some_list)
