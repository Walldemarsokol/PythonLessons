from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data
from log import *

def choice():
    print(  'Добро пожаловать в базу данных компании!\n\
            Для регистрации пользователя нажмите 1;\n \
            Для входа пользователя нажмите 2;\n\
            Для выхода из приложения нажмите 3;\n\
            При ошибке ввода можно повторить попытку.')
    data=input('Enter number: ')
    if data=='1':
        return reg_user()
    elif data=='2':
        return user_log_in()
    elif data=='3':
        return  print('Спасибо за использование программы!\n')
    else:
        print('Неправильно набрана команда\n')
        return choice()





def input_data(user):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер телефона: ")
    note = input("Введите котегорию контакта: ")
    some_list=[last_name,first_name,middle_name,brith_name,phone_number,note]
    add_data(some_list,user)
    return [last_name, first_name, middle_name, brith_name, phone_number, note]


def choice_todo(user):
    print("Выберете команду:\n\
    1 - ипорт;\n\
    2 - экспорт;\n\
    3 - поиск контакта;\n\
    4 - выход из программы.")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = None
        import_data(input_data(user), sep)
        print()
        choice_todo(user)
    elif ch == '2':
        data = export_data()
        print_data(data)
        print()
        choice_todo(user)
    elif ch== '3':
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        exp_data(word,user)
        if item != None:
            print('Фамилия'.center(20),'Имя'.center(20),'Отчество'.center(20),'Дата рождения'.center(20),'Телефон'.center(15),'Категория'.center(30))
            print('-'*130)
            print(item[0].center(20),item[1].center(20),item[2].center(20),item[3].center(20),item[4].center(15),item[5].center(30))
            print()
            choice_todo(user)
        else:
            print("Данные не обнаруженны")
            print()
            choice_todo(user)
    elif ch== '4':
        log_out(user)
        return print('Спасибо за использование программы!\n')
    else:
        print('Неверный ввод данных. Повторите попытку выбора.')
        return choice_todo(user)
    


def reg_user():
    user=input('Введите имя пользователя: ')
    with open('users.txt','a+',encoding='utf-8') as f:
        f.write('\n')
    check_name('users.txt',user) #проверяет есть ли такой пользователь.
    reg_password()
    choice()


def reg_password():  
    password=input('Введите пароль: ')
    check_pass=(input('Подтвердите пароль: '))
    if password==check_pass:    
        with open('users.txt','a',encoding='utf-8') as pas:
            pas.write('\n')
            pas.write(f'{password}')
            print('Thanks for your registration!')
            print()
    else:
        print('Пароли не совпадают.Повторите попытку.')
        print()
        return reg_password()
    
    
def check_name(file,usr):
    with open(file,'r',encoding='utf-8') as f:
        a = True
        while a:
            file_line = f.read()
            if usr in file_line:
                return check_name(file,input('Пользователь с таким именем уже зарегистрирован.\n\
                                         Введите другое имя: '))
                a=False
            else:
                with open(file,'a',encoding='utf-8') as us:
                    us.write('\n')
                    us.write(f'{usr}')
                    log_sing_up(usr)
                    a=False
                    
                    

def user_log_in():
    user=input('Enter user name: ')
    with open('users.txt','r',encoding='utf-8') as us:
        a = True
        while a:
            file_line = us.readline()
            if user in file_line:
                log_pass(user)
                a = False
            elif not file_line:
                print('Пользователь не найден.Повторите попытку.')
                return user_log_in()
                a = False
    choice_todo(user)

def control_pass(list,user,pas):
    list_new=[]
    for i in list:
        i=i.replace('\n','')
        list_new.append(i)
    for i in list_new:
        if i == user:
            index=list_new.index(user)
            if pas == list_new[index+1]:
                log_in(user)# функция для фиксации входа в систему
                return
            else:
                print("Invalid password.")
                uncorrect_password(user)#фиксация,если пароль не верный
                return log_pass(user)

def log_pass(user):
    pas=input('Enter password: ')
    with open('users.txt','r+',encoding='utf-8') as us:
        file_line = us.readlines()
        some_list=[]
        for file in file_line:
            if file=='\n':
                continue
            else:
                some_list.append(file)
    control_pass(some_list,user,pas)