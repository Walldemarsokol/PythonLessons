# value = None


# #print(type(b))
# #print(type(a))
# value =1234
# #print(type(value))
# a=1,23
# b=123

# s='hello \nworld'  #слеш и н - сносят текст на новую строку

# print(s) # вывод с
# print (b,'--',a,'---',s)

# print ('{}-{}-{}'.format(a,b,s))

# print (f'{a}-{b}-{s}')

# print ('{1}-{2}-{0}'.format(a,b,s))

# list=['reno','demo']
# print(list)

# print('Введите a:')
# a=int(input())  #если написать строчное, то просто указать input без типа данных
# print('Введите b:')
# b=int(input())# так же есть типв данных

# print(a,'+',b,'=',a+b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# Важно и нужно, без них вы не напишете ни одной
# программы
# Если помните математику – проблем не будет
# +, -,
# *
# , /, %, //,
# **
# Приоритет операций
# **
# , ⊕, ⊖,
# *
# , /, //, %, +, -
# ( ) Скобки меняют приоритет

# a=123
# b=-345
# c=a+b
# print(c)
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# range(*(1,5,2))

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,
# ^
# Кое-что ещё: is, is not, in, not in

# a=[1,2]
# b=[1,2]
# print(a==b)

# a=1>2
# print(a)

# a=1<2<5
# print(a)


# func=1
# t=4
# x=123
# print (func<t>x)

# f=1>2 or 4<6
# print(f)

# f=[1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f(0)%2 #f(0)%2==0
# print(is_odd)

# if condition:
#  # operator 1
#  # operator 2
#  # ...
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # ...
#  # operator n + m

# username = input('Введите имя: ')
# if(username == 'Маша'):
#  print('Ура, это же МАША!');
# else:
#  print('Привет, ', username);

# a=int(input('a='))
# b=int(input('b='))
# if a>b:
#     print(a)
# else:
#     print(b)

# Управляющие конструкции: if, if-else
# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator 

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)


# operator while

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # . . .
#  # operator n + m

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# else:
#  print('Пожалуй')
#  print('хватит )')
# print(inverted)
# # Пожалуй
# # хватит )
# # 32


# Когда мы знаем, что хотим
# for i in enumeration:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

# for i in 1, -2, 3, 14, 5:
# print(i)
# # 1
# # -2
# # 3
# # 14
# # 5

# list =[1,2,3,4,5]
# for i in list:
#     print(i)  #print(i**2)

# r=range(10) # выдаcт значение от 0-9
# for i in r:
#     print(i)
# r=range(1,10,2) # выдcат значения 1 3 5 7 9
# for i in r:
#     print(i)

# r='qwerty' # выдат q w e r t y
# for i in r:
#     print(i)

#вложенные циклы
# line = ""
# for i in range(5):
#  line = ""
#  for j in range(5):
#  line += "*"
#  print(line)


# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

#функции
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return

# for i in rage(1,10,2) # если стоит 3 аргумента, то первый - начало отчета, второй это крайний элемент #-1 и последний аргумент это число,что плюсуется и получается отчет 1+2(3)+2(5)+2(7)+2(9). Тобишь в #данном случае выводится нечетное
# 	print(i)

# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# # 100 80 60 40 20
# for i in range(5):
#  print(i)
# # 0 1 2 3 4
# line = ""
# for i in range(5):
#  line = ""
#  for j in range(5):
#  line += "*"
#  print(line)
# #о строках в пайтон

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#  print(c)
# print(text[0])  #c
# print(text[1])  #ъ
# print(text[len(text)])  #IndexError
# print(text[len(text)-1])  #k
# print(text[-5])   #б   если с=0 индекс,то к(в конце строки) будет иметь индекс -1.
# #следовательно если идти в лево,то минусовой индекс -5 будет иметь значение "б"
# print(text[:2])    #съ .значение в скобках это диапазон. по умолчанию пишется от нуля и можно не #указывать нуль, если нужен диапазон от нуля. Если нужен другой диапазон, то нужно указать индекс
# # если написать print(text[:]) то выдаст значение от 0 и до length ,тобишь все

# print(text[6:-18]) # значит, что значение диапазона будет с начала строки на 6 индексе и с конца #строки на -18 индексе. "еще этих мягких"

# #если не знаю какое значение имеет определенный синтаксис, то можно поступить так: 
# ввести help(запрашиваемый синтаксис) и запустить программу. нам дадут справку о строке

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] #

# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
# Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers)        # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)        # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(f'{len(numbers)}len')
# print(numbers)        # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i)             # [20, 4, 6, 8, 10]
# print(numbers)        # [10, 2, 3, 4, 5]

# #если хотим преобразовать тип данных range в тип данных list потребуется сделать вот что:

# ran=range(1,6)
# numbers=list(ran)


# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент	

# #Это фрагмент программы, используемый
# #многократно
# def function_name(x):
# # body line 1
# # . . .
# # body line n
#  # optional return	


# def f(x):
#  return x**2
# def f(x):
#  if x == 1:
#  return 'Целое'
#  elif x == 2.3:
#  return 23
#  else:
#  return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType

def f(x):
 return x**2
def f(x):
 if x == 1:
    return 'Целое'
 elif x == 2.3:
    return 23
 else:
    return                      
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType
