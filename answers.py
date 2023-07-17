from flask import redirect
import json
f = open('db.json', 'r')
hello_text = """
Вас приветствует Тандыр Эт
Выберите команду:
1 Показать меню
2 Показать контакты
3 Показать все точки 
"""
menu1 = json.load(f)
def menu(text):
    test = ''
    if '1' in text:
        for i in menu1:
            test += f"{i['title']} {i['description']} {i['image']}"
        print(test)
        return str(test)
    else:
        return 'ewtsf'