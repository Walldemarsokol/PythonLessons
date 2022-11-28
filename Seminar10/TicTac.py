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
                for row in range(len(self.field)):
                    for col in range(len(self.field)):
                        if self.field[0].count(self.field[0][0])==3 and self.field[0][0]!='-':
                            self.end_of_game=True
                            self.win=self.field[row][col]
                            return f'Победил игрок {self.field[row][col]}'
                        elif self.field[row][col]==3 and self.field[row][col]!='-':
                            self.end_of_game=True
                            self.win=self.field[row][col]
                            return f'Победил игрок {self.field[row][col]}'
                        elif self.field[2][0]==self.field[1][1]==self.field[0][2] and self.field[2][0]!='-':
                            self.end_of_game=True
                            self.win=self.field[2][0]
                            return f'Победил игрок {self.field[row][col]}'
                else:
                        return 'Продолжаем играть'
                        
            # if self.field[0].count(self.field[0][0])==3 and self.field[0][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][0]
            #     return f'Победил игрок {self.field[0][0]}'

            # elif self.field[0][0]==self.field[1][0]==self.field[2][0] and self.field[0][0]!='-':
            #     self.end_of_game=True
            #     self.win=self.field[0][0]
            #     return f'Победил игрок {self.field[0][0]}'

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
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 3))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 3))
print(*board.get_field(), sep="\n")
print(board.make_move(3, 1))
print(board.make_move(3, 3))
print(*board.get_field(), sep="\n")
# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Эта клеточка уже занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья!")
#             break
#     draw_board(board)

# main(board)