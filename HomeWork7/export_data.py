#модуль экспорта
from log import exp_data

def export_data():
    with open('phone.csv', 'r', encoding='utf-16') as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
            elif ';' in line:
                temp = line.splin().split(';')
                data.append(temp)
            elif ':' in line:
                temp = line.splin().split(':')
                data.append(temp)
            elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data