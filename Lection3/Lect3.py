#lamda function


# list=[ (i,i) for i in range(1,21) if i%2==0]  #это пример лямбда функции, которая вызывается например разово. 
#в этом примере еще и создали кортежи из четных чисел диапазона 
# def f(x):
#     return x**3


# list=[f(i) for i in range(1,21) if i%2==0] 

# print(list)
# def select(f,col):
#     return [f(x) for x in col ]

# def where (f, col):
#     return [x for x in col if f(x)]

# data='1 2 3 5 8 15 23 38'.split()

# res=select(int,data)
# res = where(lambda x: not x%2, res)
# res = select(lambda x:(x,x**2),res)
# print(res) 

# li=[x for x in range(1,20)]

# li=list(map(lambda x:x+10,li))

# print(li)

 
# data=list(map(int,'2 3 4 543 32 2 4'.split()))
# print(data)
# for e in data :
#     print(e)

# def where (f, col):
#     return [x for x in col if f(x)]

# data='1 2 3 5 8 15 23 38'.split()

# res=map(int,data)
# res = where(lambda x: not x%2, res)
# res = list(map(lambda x:(x,x**2),res))
# print(res) 

# data=[x for x in range(10)]

# res=list(filter(lambda x: not x%2,data) 

# print(res)


# data='1 2 3 5 8 15 23 38'.split()

# res=map(int,data)
# res = filter(lambda x: not x%2, res)
# res = list(map(lambda x:(x,x**2),res))
# print(res) 


# users = ['user1','user2','user3','user4','user5']
# ids =[4,5,9,14,7]
# res=list(zip(users,ids)) #функция делает соединение двух списков и добавляет их значения в кортежи
# print(res)

# users = ['user1','user2','user3','user4','user5']
# ids =[4,5,9,14,7]
# res=list(enumerate(users))  #функция enumirate пронумеровывает елемнты списка
# print(res)