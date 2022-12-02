# class MinStat:
#     def __init__(self):
#         self.some_list=[]
    
#     def add_number(self,number):
#         self.some_list.append(number)
        
#     def result(self):
#         if self.some_list==[]:
#             return None
#         else:
#             return min(self.some_list)
    
# class MaxStat:
#     def __init__(self):
#         self.some_list=[]
    
#     def add_number(self,number):
#         self.some_list.append(number)
        
#     def result(self):
#         if self.some_list==[]:
#             return None
#         else:
#             return max(self.some_list)
    
# class AverageStat:
#     def __init__(self):
#         self.some_list=[]
    
#     def add_number(self,number):
#         self.some_list.append(number)
        
#     def result(self):
#         if self.some_list==[]:
#             return None
#         else:
#             l=len(self.some_list)
#             n=sum(self.some_list)
#             return n/l


# values = [1, 2, 4, 5]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
    
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


class Table:
    
    def __init__(self,rows, cols):
        self.field = [ [0 for _ in range(cols)] for _ in range(rows) ]
        self.rows = rows
        self.cols = cols
        
    def get_value(self, row, col):
        if  row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        else:
            return None
 
    def set_value(self, row, col,value):
        self.field[row][col] = value
    
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols

    def add_row(self,row):
        return self.field[row]
            
    
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
    
tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()