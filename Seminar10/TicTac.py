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
    
        
        #для проверки, есть ли победитель.
        # Метод возвращает Х,если победил первый игрок.О если второй игрок,
        # D - если ничья и None если можно продолжать игру
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
                    
                    self.field = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
                    for each in self.field:
                        if self.field[each[0]] == self.field[each[1]] == self.field[each[2]]:
                            return self.field[each[0]]
                    return False
            # if self.field[0].count(self.field[0][0])==3 and self.field[0][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][0]
            #     return f'Победил игрок {self.field[0][0]}'
            # elif self.field[1].count(self.field[1][0])==3 and self.field[1][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[1][0]
            #     return f'Победил игрок {self.field[1][0]}'
            # elif self.field[2].count(self.field[2][0])==3 and self.field[2][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[2][0]
            #     return f'Победил игрок {self.field[2][0]}'
            # elif self.field[0][0]==self.field[1][0]==self.field[2][0] and self.field[0][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][0]
            #     return f'Победил игрок {self.field[0][0]}'
            # elif self.field[0][1]==self.field[1][1]==self.field[2][1] and self.field[0][1]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][1]
            #     return f'Победил игрок {self.field[0][1]}'
            # elif self.field[0][2]==self.field[1][2]==self.field[2][2] and self.field[0][2]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][2]
            #     return f'Победил игрок {self.field[0][2]}'
            # elif self.field[0][0]==self.field[1][1]==self.field[2][2] and self.field[0][2]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][0]
            #     return f'Победил игрок {self.field[0][2]}'
            # elif self.field[2][0]==self.field[1][1]==self.field[0][2] and self.field[2][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[2][0]
            #     return f'Победил игрок {self.field[2][0]}'
            # elif self.field[0].count('-')==3 and self.field[1].count('-')==3 and self.field[2].count('-')==3:
            #     self.end_of_game=True
            #     self.win='ничья'
            #     return 'Ничья'
            # else:
            #     return 'Продолжаем играть'
            

board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False