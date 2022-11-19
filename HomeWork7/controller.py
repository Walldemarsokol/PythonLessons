from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
from user_login import *
from registration import reg_user

def greeting():
    print('Добро пожаловать в базу данных компании!\n\
            Для регистрации нажмите 1;\n \
            Для входа по имени + пароль нажмите 2;\n\
            При ошибке ввода можно повторить попытку.\n')

def choice():
    data=input('Enter number: ')
    if data=='1':
        return reg_user()
    elif data=='2':
        return user_log_in()
    else:
        return choice(input('Введите 1 или 2: '))
        

def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите котегорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def choice_todo():
    print("Выберете команду:\n\
    1 - ипорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = None
        import_data(input_data(), sep)
    elif ch == '2':
        data = export_data()
        print_data(data)
    elif ch== '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print('Фамилия'.center(20),'Имя'.center(20),'Отчество'.center(20),'Дата рождения'.center(20),'Телефон'.center(15),'Категория'.center(30))
            print('-'*130)
            print(item[0].center(20),item[1].center(20),item[2].center(20),item[3].center(20),item[4].center(15),item[5].center(30))
        else:
            print("Данные не обнаруженны")
    else:
        print('Неверный ввод данных. Повторите попытку выбора.')
        return choice_todo()