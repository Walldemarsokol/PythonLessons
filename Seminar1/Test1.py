# Задача 1. напишите программу которая принимает на вход два числа и проверяет является ли одно из них квадратом другого

# a=int(input('введите число 1 '))
# b=int(input('введите число 2 '))

# if a**2==b or b**2==a:
#     print('Да,является')

# else:
#     print(' нет')

# Задача 2. напишите программу, которая на вход принимает 5 чисел и находит наибольшее из них

# list=map(int,input('введите числа через пробел ').split())

# max_number = max((list))
# print(max_number)

# number = int(input())
# max=number

# for _ in range(4):
#     number = int(input())
#     if number > max:
#         max=number
# print(max)

# some_list=[]
# for _ in range(5):
#     number = int(input())
#     some_list.append(number) #функция аппенд добавляет в конец листа введеннео значение
# max=some_list[0]
# for element in some_list:
#     if element > max:
#         max = element
# print( max) 

# print(max(map(int,input('введите числа через пробел  ').split())))


#Задача 3. напишите программу. где на вход принимаем число Н и выводятся значения от -н до н

# n=int(input('введите число Н '))
# some_list=[]
# for a in range(-n,n+1):
#     some_list.append(a)
# print(some_list)

# n=int(input('введите число Н '))
# for a in range(-n,n):
#         print(a, end=', ')
# print(n)

# n=int(input('введите число Н '))
# print(*range(-n,n+1), sep=', ')
# print(list(range(-n,n+1), sep=', '))

#Задача 4.напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

# print(int(float(input('введите дробное число ')) * 10) % 10)

# y = input()
# if '.' in y:
#     print(int((float(y) * 10) % 10))
    
# else:
#     print('no')

# y = float(input())
# if y%1==0:
#     print('no')
# else:
#     print(int(y * 10) % 10)

# n=input()
# if '.' in n:
#     index_t=n.find('.')
#     print(n[index_t+1])
# else:
#     print('no')

# Задача 5. напишите программу, которая принимает на вход число и проверяет кратно ли оно 5, 10, 15, но не 30

# n=int(input())
# if (n%5==0 and n%10==0 or n%15==0) and n%30 !=0:
#     print("Yes")
# else:
#     print('No')

# n = int(input())
# print('Да' if (n%5==0 and n%10==0) or (n%15==0 and n%30!=0) else 'Нет')
