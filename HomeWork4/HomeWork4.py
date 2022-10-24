
# Задача 1.Вычислить число c заданной точностью d

# n=float(input('Введите число: '))
# s=input('Введите точность: ')
# if len(s)>1:
#     s=s.replace('.','')
#     s=list(s).pop(0)
#     print(round(n,len(s)))
# if int(s)==1:
#     n=str(n)
#     print(n[0])

# Задача 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# n=int(input('Enter number: '))
# some_list=[]
# for i in range(2,n+1):
#     if n%i==0:
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#         else:
#             some_list.append(i)
# print(some_list)

# Задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# n=int(input('Enter Length: '))
# some_list=[]
# print('Enter numbers: ')
# for _ in range(n):
#     some_list.append(input())
# print(set(some_list))

#Задача 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# import random
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')
