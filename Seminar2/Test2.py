# test11 Напишите программу, которая принимает на вход число N и выдает последовательность из N членов:
# N=5:1,-3,9,-27,81
# n=int(input())
# for i in range(n-1):
#     print((-3)**i, end=",")
# else:
#   print((-3)**(n-1))

# n=int(input())
# for i in range(n-1):
#     print((-3)**i, end=",")
# print((-3)**(n-1))

# n=int(input())
# a=[]
# for i in range(n):
#     a.append((-3)**i)
# print(*a,sep=',')

#test12 Для натурального числа Н создать словарь индекс-значение, состоящий из элементов оследовательностью 3н+1
# н=6: {1:4,2:7,3:10,4:13,5:16,6:19}
# n=int(input())
# array=[]
# for i in range(1,n+1):
#     array.append(f'{i}:'+str(3*i+1))
# print(array)

# n=int(input())
# print('{',end='')
# for i in range(1,n):
#     print(f'{i}:{3*i+1}',end=',')
# print(f'{n}:{3*n+1}',end='}')

#test13. Напишите программу, в которой 
# пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# some_str_1=input()
# some_str_2=input()
# print(some_str_1.count(some_str_2) or some_str_2.count(some_str_1))

# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
# if some_str_1[i:i + len_str_2] == some_str_2:
# count += 1
# i += 1
# print(count)

# some_str_1 = input()
# some_str_2 = input()
# len_str_2 = len(some_str_2)
# i = 0
# count = 0
# while i < len(some_str_1):
# if some_str_1[i:i + len_str_2] == some_str_2:
# count += 1
# i += len_str_2
# else:
# i += 1
# print(count)