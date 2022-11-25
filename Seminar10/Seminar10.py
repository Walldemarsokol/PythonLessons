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
