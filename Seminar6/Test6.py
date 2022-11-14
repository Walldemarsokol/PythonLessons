# # Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. Приоритет операций стандартный

# def add(a, b):
#     return a + b


# def diff(a, b):
#     return a - b


# def mult(a, b):
#     return a * b


# def delim(a, b):
#     return a / b


# def app(txt):
#     sign = ''
#     for s in '+-*/':
#         if s in txt:
#             sign = s
#             break
#     if sign == '':
#         return int(txt)
#     else:
#         a, b = txt.split(sign, 1)
#         if sign == '*': return mult(app(a), app(b))
#         elif sign == '/': return delim(app(a), app(b))
#         elif sign == '+': return add(app(a), app(b))
#         elif sign == '-': return diff(app(a), app(b))


# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. Приоритет операций стандартный
# def add(lst):
#     return sum(lst)


# def diff(lst):
#     res = lst[0]
#     for i in lst[1:]:
#         res -= i
#     return res


# def mult(lst):
#     res = lst[0]
#     for i in lst[1:]:
#         res *= i
#     return res


# def delim(lst):
#     res = lst[0]
#     for i in lst[1:]:
#         res /= i
#     return res


# def app(txt):
#     if '(' in txt:
#         start = 0
#         for i in range(len(txt)):
#             if txt[i] == '(':
#                 start = i
#         fin = start + txt[start:].index(')')
#         tmp = txt[start+1:fin]
#         result = app(tmp)
#         return app(f'{txt[:start]}{result}{txt[fin+1:]}')
#     sign = ''
#     for s in '+-*/':
#         if s in txt:
#             sign = s
#             break
#     if sign == '':
#         return int(txt)
#     else:
#         lst = list(map(app,txt.split(sign)))
#         if sign == '*': return mult(lst)
#         elif sign == '/': return delim(lst)
#         elif sign == '+': return add(lst)
#         elif sign == '-': return diff(lst)


# print(app('11+7*4-4/2+3'))
# print(app('11+7+3'))
