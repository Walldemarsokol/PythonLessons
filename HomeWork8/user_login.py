from log import *



#метод входа пользователя и логгер входа
def user_log_in():
    user=input('Enter user name: ')
    with open('users.txt','r',encoding='utf-8') as us:
        # us.readline()
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

def log_pass(user):
    pas=input('Enter password: ')
    with open('users.txt','r+',encoding='utf-8') as us:
        # us.readline()
        a = True
        while a:
            file_line = us.readline()
            if pas in file_line:
                log_in(user)# функция для фиксации входа в систему
                print(f'Welcome,{user}!')
                print()
                a = False
            elif not file_line:
                print('Пароль неверный. Повторите попытку.')
                print()
                uncorrect_password(user)#фиксация,если пароль не верный
                return log_pass(user)
                a = False