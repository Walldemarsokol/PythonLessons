from log import log_sing_up

def reg_user():
    user=input('Введите имя пользователя: ')
    with open('users.txt','a+',encoding='utf-8') as f:
        f.write('-----\n')
    check_name('users.txt',user) #проверяет есть ли такой пользователь.
    log_sing_up(user)
    reg_password()


def reg_password():  
    password=input('Введите пароль: ')
    check_pass=(input('Подтвердите пароль: '))
    if password==check_pass:    
        with open('users.txt','a',encoding='utf-8') as pas:
            pas.write(f'{password}\n')
            pas.write('\n')
            print('Thanks for your registration!')
            print()
    else:
        print('Пароли не совпадают.Повторите попытку.')
        print()
        return reg_password()
    
    
def check_name(file,usr):
    with open(file,'r',encoding='utf-8') as f:
        f.readline()
        if usr in f:
            return check_name(file,input('Пользователь с таким именем уже зарегистрирован.\n\
                                         Введите другое имя: '))
        else:
            with open(file,'a',encoding='utf-8') as us:
                us.write(f'{usr}\n')