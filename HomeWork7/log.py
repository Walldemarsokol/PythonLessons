from datetime import datetime

def log_in(data):# функция для фиксации входа в систему
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a+', encoding='utf-8') as file:
        file.write(f'пользователь {data} вошел в систему в {time}\n')
        
def log_sing_up(data):# фиксация регистрации пользователя
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a+', encoding='utf-8') as file:
        file.write(f'пользователь {data} зарегистрирован в системе в {time}\n')
        
def log_out(data):# функция для фиксации выхода из системы
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a+', encoding='utf-8') as file:
        file.write(f'пользователь {data} вышел из системы в {time}\n')

def uncorrect_password(data):# функция для фиксации попытки входа в систему
    time = datetime.now().strftime('%H:%M')
    with open('log.csv', 'a+', encoding='utf-8') as file:
        file.write(f'Была попытка входа в систему.Неправильно ввели пароль. {data} пытался войти в систему в {time}\n')