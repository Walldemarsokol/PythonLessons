# class Auto:
# # атрибуты класса
# auto_name = "Lexus"
# auto_model = "RX 350L"
# auto_year = 2019
# # методы класса
# def on_auto_start(self):
# print(f"Заводим автомобиль")
# def on_auto_stop(self):
# print("Останавливаем работу двигателя")


# a = Auto()
# print(a)
# print(type(a))
# print(a.auto_name)
# a.on_auto_start()
# a.on_auto_stop()
            


# <__main__.Auto object at 0x0000001381FD8B38>
# <class '__main__.Auto'>
# Lexus
# Заводим автомобиль
# Останавливаем работу двигателя

# class Auto:
# # атрибуты класса
#     auto_count = 0

#     def __init__(self, auto_name, auto_model, auto_year):
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year

# # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         # self.auto_name = auto_name
#         # self.auto_model = auto_model
#         # self.auto_year = auto_year
#         # Auto.auto_count += 1


# a=Auto('Audi','RS6',2016)
# print(a.auto_name)
        

# a = Auto()
# a.on_auto_start('Audi','A4',2015)
# print(a.auto_name)
# print(a.auto_model)
# print(a.auto_year)

# b=Auto()
# b.on_auto_start('BMW','M5',2018)
# print(b.auto_name)
# print(b.auto_model)
# print(b.auto_year)

#Написать класс литллБелл который при вызове метода соунд будет писать динг

# class LitlleBell:
#     def sound(self):
#         print('ding')

# bell=LitlleBell()
# bell.sound()
# bell.sound()
# bell.sound()

# class Button:
#     count = 0

#     def click(self):
#         Button.count +=1

#     def click_count(self):
#         return Button.count
    
#     def reset(self):
#         Button.count=0


# button=Button()
# button.click()
# button.click()
# button.click()
# button.count()
# button.click()
# button.count()
# button.reset()
# button.count()


# class Balance:
#     weigth_r=0
#     weigth_l=0

#     def add_rigth(self,weigth_r):
#         self.weigth_r=weigth_r


#     def add_left(self,weigth_l):
#         self.weigth_l=weigth_l


#     def result(self):
#         if self.weigth_r>self.weigth_l:
#             return 'R'
#         elif self.weigth_l >self.weigth_r:
#             return 'L'
#         else:
#             return '='  

# balance = Balance()
# balance.add_rigth(10)
# balance.add_left(9)
# balance.add_left(2)
# print(balance.result())

# balance2=Balance()
# balance.add_rigth(1)
# balance.add_left(2)
# print(balance.result())

# class BigBell:
#     count=0

#     def sound(self):
#         if BigBell.count %2==0:
#             print('ding')
#         if BigBell.count %2!=0:
#             print('dong')

#         BigBell.count+=1

# bell=BigBell()
# bell.sound()
# bell.sound()
# bell.sound()

# class OddEvenSeparator():
#     def __init__(self):
#         self.l1=[]
#         self.l2=[]
    
#     def add_number(self,number):
#         if number%2==0:
#             self.l1.append(number)
#         else:
#             self.l2.append(number)

#     def even(self):
#         return self.l1
    
#     def odd(self):
#         return self.l2

    
# a=OddEvenSeparator()
# a.add_number(5)
# a.add_number(10)
# a.add_number(2)
# a.add_number(15)

# print(a.even())
# print(a.odd())

class MinMaxWordFinder:
    def __init__(self):
        self.text_list = []

    def add_sentence(self, sentence):
        words = sentence.split()
        self.text_list.extend(words)


    def shortest_words(self):
        minn = self.text_list[0]
        for word in self.text_list:
            if len(word) < len(minn):
                minn = word
        # short_list = []
        # for word in self.text_list:
        #     if len(word) == len(minn):a
        #         short_list.append(word)
        short_list = list(filter(lambda x: len(x) == len(minn), self.text_list))
        return sorted(short_list)

    def longest_words(self):
        maxx = self.text_list[0]
        for word in self.text_list:
            if len(word) > len(maxx):
                maxx = word
        short_list = list(filter(lambda x: len(x) == len(maxx), self.text_list))
        return sorted(list(set(short_list)))
a = MinMaxWordFinder()
a.add_sentence('abc abc ds')
a.add_sentence('sd fd fd nba')
print(a.shortest_words())
print(a.longest_words())

    
        # short_list=[]
        # for word in self.text_list:
        #     if len(word) == len(minn):
        #         minn=word
        #         short_list.append(word)

a=MinMaxWordFinder()
a.add_sentence('abc abc asdasdasdas')
a.add_sentence('asda adad dasdasd dda')
print(a.shortest_words())
print(a.longest_words())

