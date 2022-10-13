

# редактирование
# with open('file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')



# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLINE 2\n') 
# data.write('LINE 2\n') 
# data.close()



# exit()   #need for exit of programm
#считывание
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()

# exit()

# # import Lect  - если запрос прямой, можно сделать как ниже. задать алиас для запроса
# import Lect as L  #таким образом можно делать запрос, но более коротко
# print(L.f(1))


# def new_string(symbol, count):  -тут не указан каунт, и если не указать кол-во в нем, то будет ошибка
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required 
# если создать в каунт уже кол-ве изначально, напирмер count = 3, то можно или не указвать
# кол-во и будет выдавать множитель 3, или можно указать множитель и он будет задавать значение
# print(new_string('!', 5)) # !!!!!

# print(new_string(4)) # 12- если передать число, то будет умножение числа на значение аргумента

# def concatenatio(*params):  # для написание неограниченного набора аргументов савится звездочка
#  res: str = ""
#  for item in params:
#  res += item
#  return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw  # и можно указать почти любое множество
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# рекурсия
# def fib(n):
#  if n in [1, 2]:
#  return 1
#  else:
#  return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# кортежи - это неизменяемые списки, т.е. неьзя редактироват или присваивать значения


# # a,b = 3,4 - классическое присвоение а(3) и в(4)
# a= (3,41,1,4)  #это уже кртеж

# print(a)
# print(a[-1])  #обращение к конкретному элементу

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support
# item assignment

# a=(3,4,5)
# for item in a:
#     print(item)  # 3 4 5

#     t = tuple(['red', 'green', 'blue'])  #преобразование списка в кортеж
# red, green, blue = t    # преобразование кортежа в независимые переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))  #и далее работаем с ними как с независимыми переменными
# # r:red g:green b:blue



# Словари
# Неупорядоченные коллекции произвольных
# объектов с доступом по ключу
# dictionary = {}  # создаем пустой словарь
# dictionary = \
#  {
#  'up': '↑',     # слева ключ, а справа его значение. пишутся через " : "
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  }
# print(dictionary['up'])  #сначала распечатается стрелочка, а потом уже указание слова
# dictionary['up'] = 'up'
# print(dictionary['up'])
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←    обращение к ключу через квдратные скобки, что бы получить значение ключа
# # типы ключей могут отличаться

# for k in dictionary.keys():
#     print(k) 

# for k in dictionary.values():  #если нужны конкретные значения, то запросим так
#     print(k) 
#или еще подругому находим только значения
# for v in dictionary:
#     print(dictionary[v])

# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')   #delete elements
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}

# s=frozenset(a)  #замороженное множество


# list1 = [1,2,3,4,5]
# list2=list1
# list1[0] = 123
# list2[1] = 234
# for e in list1:
#     print(e)

# print()
# for e in list2:
#     print(e)
# print(len(list1))  #удаляет каждый последний элемент или заданный
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.insert(2,11)) #добавит перед 2 индексом заданный элемент
# print(list1)

# print(list1.append(11)) #добавит в конец заданный элемент
# print(list1)