class TicTacToeBoard:
    def __init__(self):
        self.field=[]
        for row in range(3):
            r=[]
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.move_x=True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True

    def new_game(self):#start new game
        self.field=[]
        for row in range(3):
            r=[]
            for col in range(3):
                r.append('-')
            self.field.append(r)
        self.move_x=True
        self.end_of_game = False
        self.winner = None
        self.win = ''
        self.first_move = True
        
    def get_field(self):#для получения поля(список списков).
        return self.field #При каждом вызове появляется обновленное поле
    
    def check_field(self):
        if self.win=='ничья':
            return 'D'
        elif self.win == 'X':
            return 'X'
        elif self.win=='O':
            return 'O'
        else:
            return None
        
    def make_move(self,row,col):
        
        if self.end_of_game and not self.first_move:
            return 'Игра уже завершена'
        else:
            if self.field[row-1][col-1]!='-':
                return f'Клетка {row},{col} уже занята'
            else:
                if self.move_x:
                    self.field[row-1][col-1]='X'
                    self.move_x=False
                    self.first_move=False
                else:
                    self.field[row-1][col-1]='O'
                    self.move_x=True
                    self.first_move=False
                for row in range(len(self.field)):
                    if self.field[row].count(self.field[row][0])==3 and self.field[row][0]!='-':
                        self.end_of_game=True
                        self.win=self.field[row][0]
                        return f'Победил игрок {self.field[row][0]}'
                    elif self.field[0].count('-')==3 and self.field[1].count('-')==3 and self.field[2].count('-')==3:
                        self.end_of_game=True
                        self.win='ничья'
                        return 'Ничья'
                    for col in range(len(self.field)):
                        if self.field[row][col]==self.field[col][col]==self.field[2][col] and self.field[row][col]!='-':#проверка столбиков
                            self.end_of_game=True
                            self.win=self.field[row][col]
                            return f'Победил игрок {self.field[row][col]}' 
                        #проверка диагоналей
                        elif self.field[row][col]==self.field[1][1]==self.field[2][2] and self.field[row][col]!='-' or self.field[row][2]==self.field[1][1]==self.field[2][row] and self.field[row][2]!='-':
                            self.end_of_game=True
                            self.win=self.field[1][1]
                            return f'Победил игрок {self.field[1][1]}'
                    else:
                        return 'Продолжаем играть'
    

# board = TicTacToeBoard()#проверка строки
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 2))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 3))
# print(board.make_move(2, 3))
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 1))
# print(board.make_move(3, 3))
# print(*board.get_field(), sep="\n")

# board = TicTacToeBoard()#проверка столбиков 1
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")

# board = TicTacToeBoard()#проверка столбиков3
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 3))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(2, 3))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(3, 3))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 2))#x
# print(*board.get_field(), sep="\n")

# board = TicTacToeBoard() #проверка столбиков2
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 3))
# print(*board.get_field(), sep="\n")
# print(board.make_move(3, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 3))

# board = TicTacToeBoard()#проверка диагон1
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 2))
# print(board.make_move(2, 2))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(3, 3))#x
# print(*board.get_field(), sep="\n")

# board = TicTacToeBoard()#проверка диагон2
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 3))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 2))
# print(board.make_move(2, 2))#x
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(3, 1))#x
# print(*board.get_field(), sep="\n")
