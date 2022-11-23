# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:

# new_game() – для создания новой игры;
# get_field() – для получения поля (список списков);
# check_field() – для проверки, есть ли победитель, который возвращает X, если победил первый игрок, 0, если второй, D, если ничья и None, если можно продолжать игру;
# make_move(row, col) – который устанавливает значение текущего хода в ячейку поля с координатами row, col, если это возможно, «переключает» ход игрока, а также возвращает сообщение «Победил игрок X» при победе крестиков, «Победил игрок 0» при победе ноликов, «Ничья» в случае ничьей и «Продолжаем играть», если победитель после данного хода неопределён.
# Кроме того, метод make_move должен возвращать сообщение «Клетка <row>, <col> уже занята», если в клетке уже стоит крестик или нолик, и «Игра уже завершена», если в текущей игре уже выявлен победитель или закончились ячейки для ходов.

# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col метода make_move могут принимать значения от 1 до 3.

# Пример: 
# board = TicTacToeBoard()
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(*board.get_field(), sep="\n")
# print(board.make_move(1, 1))
# print(board.make_move(1, 2))
# print(*board.get_field(), sep="\n")
# print(board.make_move(2, 1))
# print(board.make_move(2, 2))
# print(board.make_move(3, 1))
# print(board.make_move(2, 2))
# print(*board.get_field(), sep="\n")


class TicTacToeBoard:
    
    def new_game(self):#start new game
        p=0
        
    def get_field(self):#для получения поля(список списков)
        s=0
        
        #для проверки, есть ли победитель.
        # Метод возвращает Х,если победил первый игрок.О если второй игрок,
        # D - если ничья и None если можно продолжать игру
    def check_field(self):
        r=0
        
    def make_move(row,col):
        e=0

    