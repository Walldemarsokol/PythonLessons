# Чтобы работать с
# унаследованными атрибутами, нужно их перечислить, например, super().__init__(color, param_1,param_2). 


# class Shape:
#     def __init__(self, color, param_1, param_2):
#         self.color = color
#         self.param_1 = param_1
#         self.param_2 = param_2
#     def square(self):
#         return self.param_1 * self.param_2

# class Rectangle(Shape):
#     def __init__(self, color, param_1, param_2, rectangle_p):
#         super().__init__(color, param_1, param_2)
#         self.rectangle_p = rectangle_p
#     def get_r_p(self):
#         return self.rectangle_p
# class Triangle(Shape):
#     def __init__(self, color, param_1, param_2, triangle_p):
#         super().__init__(color, param_1, param_2)
#         self.triangle_p = triangle_p
#     def get_t_p(self):
#         return self.triangle_p
# r = Rectangle("white", 10, 20, True)
# print(r.color)
# print(r.square())
# print(r.get_r_p())
# t = Triangle("red", 30, 40, False)
# print(t.color)
# print(t.square())
# print(t.get_t_p())
    
# 
# class Player:
#     def player_method(self):
#         print("Родительский метод класса Player")
# class Navigator:
#     def navigator_method(self):
#         print("Родительский метод класса Navigator")
# class MobilePhone(Player, Navigator):
#     def mobile_phone_method(self):
#         print("Дочерний метод класса MobilePhone")

# m_p = MobilePhone()
# m_p.player_method()
# m_p.navigator_method()
# m_p.mobile_phone_method()
# 


# Возможна ситуация, когда у классов-родителей совпадают имена атрибутов и методов. Тогда
# обращение к такому атрибуту или методу через «наследник» будет адресовано к атрибуту или методу
# того класса-родителя, который значится первым.
# 
# class Shape:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#     def get_params(self):
#         return f"Параметры Shape: {self.param_1}, {self.param_2}"
# class Material:
#     def __init__(self, param_1, param_2):
#         self.param_1 = param_1
#         self.param_2 = param_2
#     def get_params(self):
#         return f"Параметры Material: {self.param_1}, {self.param_2}"
# class Triangle(Shape, Material):
#     def __init__(self, param_1, param_2):
#         super().__init__(param_1, param_2)
#         pass
# t = Triangle(10, 20)
# print(t.get_params())

# Перегрузка методов
# Реализуется в возможности метода отражать разную логику выполнения в зависимости от количества
# и типа передаваемых параметров.
# класс Auto
# class Auto:
#     def auto_start(self, param_1, param_2=None):
#         if param_2 is not None:
#             print(param_1 + param_2)
#         else:
#             print(param_1)
# a = Auto()
# a.auto_start(50)
# a = Auto()
# a.auto_start(10,12)

# Переопределение методов
# Переопределение методов в полиморфизме выражается в наличии метода с одинаковым названием
# для родительского и дочернего классов. При этом логика методов различается, но названия
# идентичны.
# класс Transport
# class Transport:
#     def show_info(self):
#         print("Родительский метод класса Transport")
# # класс Auto, наследующий Transport
# class Auto(Transport):
#     def show_info(self):
#         print("Родительский метод класса Auto")
# # класс Bus, наследующий Transport
# class Bus(Transport):
#     def show_info(self):
#         print("Родительский метод класса Bus")
        
# t = Transport()
# t.show_info()
# a = Auto()
# a.show_info()
# b = Bus()
# b.show_info()


# class Selector:
#     def __init__(self, values):
#         self.values = values

#     def get_odds(self):
#         odd_val = []
#         for i in range (len(self.values)):
#             if self.values[i] % 2 != 0:
#                 odd_val.append(self.values[i])
#         return odd_val

#     def get_even(self):
#         even_val = []
#         for i in range(len(self.values)):
#             if self.values[i] % 2 == 0:
#                 even_val.append(self.values[i])
#         return even_val

# values = [11,12,13,14,15,16,22,44,66]
# selector = Selector(values)
# odds = selector.get_odds()
# evens = selector.get_even()
# print(' '.join(map(str, odds)))
# print(' '.join(map(str, evens)))

# class AmericanDate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day

#     def set_year (self, year):
#         self.year = year


#     def set_moth (self, month):
#         self.month = month


#     def set_day (self, day):
#         self.day = day

#     def get_year (self, year):
#         return year

#     def get_month (self, month):
#         return month

#     def get_day (self, day):
#         return day

#     def format (self): 
#         return '{:02}.{:02}.{:04}'.format(self.month, self.day, self.year)


# class EuropeanDate:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#     def set_year(self, year):
#         self.year = year


#     def set_moth(self, month):
#         self.month = month


#     def set_day(self, day):
#         self.day = day

#     def get_year(self, year):
#         return year

#     def get_month(self, month):
#         return month

#     def get_day(self, day):
#         return day

#     def format(self):
#         return '{:02}.{:02}.{:04}'.format(self.day, self.month, self.year)

# american = AmericanDate(2000, 4, 10)
# european = EuropeanDate(2000, 4, 10)
# print(american.format())
# print(european.format())
