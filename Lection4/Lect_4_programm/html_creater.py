from user_interface import temperature_view 
from user_interface import wind_speed_view 
from user_interface import pressure_view 

def create(device=1):
    style = 'style="front-size:20px;"'   #описание стиля. Указывается размер шрифта
    html='<html>\n  <head><\head>\n  <body>\n'  #заготовка для html представления
    html +='    <p {}>Temperature:  {}  c</p>\n'\
        .format(style,temperature_view(device))  #в качестве тем-ры подсовываем значение полученное с нашего view
    html +='    <p {}>Wind_speed:  {}  m/s</p>\n'\
        .format(style,wind_speed_view(device))     #в качестве ск-ти ветра подсовываем значение полученное с нашего view
    html +='    <p {}>Pressure:  {}  mmHg</p>\n'\
        .format(style,pressure_view(device))     #в качестве давление подсовываем значение полученное с нашего view
    html += '   </body>\n</html>'

    with open('index.html','w') as page:    #для всего этого создаем файлик index.html и сохраняем его
        page.write(html)
    
    return html


def new_create(data,device=1):
    t,p,w=data  #порядок выставлен эквивалентно методу data_collection который в data_provider
    style = 'style="front-size:20px;"'   #описание стиля. Указывается размер шрифта
    html='<html>\n  <head><\head>\n  <body>\n'  #заготовка для html представления
    html +='    <p {}>Temperature:  {}  </p>\n'\
        .format(style,t)  #в качестве тем-ры подсовываем значение полученное с нашего view
    html +='    <p {}>Wind_speed:  {}  m/s</p>\n'\
        .format(style,w)     #в качестве ск-ти ветра подсовываем значение полученное с нашего view
    html +='    <p {}>Pressure:  {}  mmHg</p>\n'\
        .format(style,p)     #в качестве давление подсовываем значение полученное с нашего view
    html += '   </body>\n</html>'

    with open('new_index.html','w') as page:    #для всего этого создаем файлик index.html и сохраняем его
        page.write(html)
    
    return data