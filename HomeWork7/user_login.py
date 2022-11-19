from log import *

#метод входа пользователя и логгер входа
def user_log_in():
    user=input('Enter user name: ')
    with open('users.txt','r',encoding='utf-8') as us:
        us.readline()
        if user in us:
            log_pass(user)
        else:
            print('Пользователь не найден.Повторите попытку.')
            return user_log_in()

def log_pass(user):
    pas=input('Enter password: ')
    with open('users.txt','r+',encoding='utf-8') as us:
        us.readline()
        if pas in us:
            log_in(user)# функция для фиксации входа в систему
            print(f'Welcome,{user}!')
            print()
        else:
            print('Пароль неверный. Повторите попытку.')
            print()
            uncorrect_password(user)
            return user_log_in()