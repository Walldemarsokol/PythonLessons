x=0
y=0

def init(a,b):  #в методе мы указываем глобал для того,что бы х и у в методе могли быть зависимы от 
    global x
    global y
    x=a
    y=b

init(11,22)

print(x)
print(y)