# class Car:
#     def __init__(self,color,year,max_speed):
#         self.color = color
#         self.year = year
#         self.max_speed=max_speed

#     def __add__(self,other):
#         return self.max_speed + other.max_speed

# bmw=Car('black',2018,250)
# audi=Car('yellow',2016,240)
# print(bmw + audi)


# class Foddinfo:

#     def __init__(self,proteins,fats,carbonydrates):
#         self.proteins=proteins
#         self.fats=fats
#         self.carbonydrates = carbonydrates

#     def get_proteins(self):
#         return self.proteins
    
#     def get_fats(self):
#         return self.fats
    
#     def get_carbonydrates(self):
#         return self.carbonydrates
    
#     def get_kcalories(self):
#         kcalories = (4*self.proteins + 9*self.fats +4*self.carbonydrates)
#         return kcalories
    

#     def __add__(self,other):
#         return Foddinfo(self.proteins+other.proteins, self.fats+other.fats, self.carbonydrates+other.carbonydrates)
# food1 = Foddinfo(100,100,100)
# food2 = Foddinfo(50,60,70)
# food3=food1+food2

# print(food1.get_proteins(),food1.get_fats(),\
#         food1.get_carbonydrates(),food1.get_kcalories())
# print(food2.get_proteins(),food2.get_fats(),food2.get_carbonydrates(),food2.get_kcalories())
# print(food3.get_proteins(),food3.get_fats(),food3.get_carbonydrates(),food3.get_kcalories())


class ReversList:
    def __init__(self,some_list):
        self.some_list=some_list[::-1]

    def __getitem__(self,item):
        return self.some_list[item]
    
    def __len__(self):
        return len(self.some_list)
    
rl=ReversList([10,20,30])
for i in range(len(rl)):
    print(rl[i])