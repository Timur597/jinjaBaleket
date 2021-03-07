# from jinja2 import Template, escape

#1 Введение в модуль
######################################
# name = 'Bishkek'

# tm = Template("Hi {{ name }}")
# msg = tm.render(name=name)

# print(msg)
######################################
######################################
# name = 'Bishkek'

# tm = Template("Hi {{ name }}")
# msg = tm.render(name=name)

# msg2 = f"Hi {name}"
# print(msg, msg2, sep="\n")
######################################
# {%%} - спецификатор шаблона
# {{}} - выражение для вставки конструкции в Python шаблона
# {##} - блок комментариев
# # ## - строковый комментарий
######################################
# name = 'Bishkek'
# age = 28

# tm = Template("Hi {{ n }} youe age {{ a }}")
# msg = tm.render(n=name, a=age)

# print(msg)
######################################
# name = 'Bishkek'
# age = 28

# tm = Template("Hi {{ n.upper() }} youe age {{ a**2 }}")
# msg = tm.render(n=name, a=age)

# print(msg)
######################################
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# per = Person("Kairat", 33)

# tm = Template("Мне {{p.age}} лет и зовут {{p.name}}.")
# msg = tm.render(p = per)

# print(msg)
#######################################
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def getName(self):
#         return self.name

#     def getAge(self):
#         return self.age

# per = Person("Name", 33)

# tm = Template("Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}.")
# msg = tm.render(p = per)

# print(msg)
#######################################
# per = {'name': 'Bishkek', 'age' : 25}

# tm = Template("Мне {{ p.age }} лет и зовут {{ p.name }}.")
# msg = tm.render(p = per)

# print(msg)
#######################################
# per = {'name': 'Bishkek', 'age' : 21}

# tm = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}.")
# msg = tm.render(p = per)

# print(msg)
#######################################





#2  Экранирования и блоки raw, for, if
#######################################
# data = '''\tМодуль дзиньдзя 
#         вместо определения 
#         {{ name }} подставляет 
#         соответствующие значения'''

# tm = Template(data)
# msg = tm.render(name = "Bishkek")

# print(msg)
#######################################
# data = '''\t{% raw %}Модуль дзиньдзя 
#         вместо определения 
#         {{ name }} подставляет 
#         соответствующие значения{% endraw %}'''

# tm = Template(data)
# msg = tm.render(name = "Bishkek")

# print(msg)
#######################################
# Открыть в HTML
# link = '''В HTML ссылки определяются так: 
# <a href="#">Ссылка </a>'''

# tm = Template(link)
# msg = tm.render()

# print(msg)

# <a href="#">Ссылка </a>' |==>> В HTML-документе ссылки определяются так:Ссылка
# e - escape (экранирование)
#######################################
#Открыть в HTML
# link = '''В HTML ссылки определяются так: 
# <a href="#">Ссылка </a>'''

# tm = Template("{{link | e}}")
# msg = tm.render(link=link)

# print(msg)
########################################
# Открыть в файл.html
# В HTML ссылки определяются так: 
# &lt;a href=&#34;#&#34;&gt;Ссылка &lt;/a&gt;
# e - escape (экранирование)
#########################################

# link = '''В HTML ссылки определяются так: 
# <a href="#">Ссылка </a>'''

# msg = escape(link)

# print(msg)

#####################################
# Блок for 
# {% for <выражение> -%}
#     <повторяемый фрагмент>
# {% endfor %} 
#######################################

# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities %}
#                     <option value="{{c["id"]}}">{{c['city']}}</options>
#                 {% endfor %}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)
#######################################
#без переноса строки
# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities %}<option value="{{c["id"]}}">{{c['city']}}</options>{% endfor %}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)
######################################
#{% for c in cities -%} минус для упорядовачивания 
# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities -%}
#                     <option value="{{c["id"]}}">{{c['city']}}</options>
#                 {% endfor -%}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)
########################################
# if блоки 
# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities -%}
#                 {% if c.id > 6 -%}
#                     <option value="{{c["id"]}}">{{c['city']}}</options>
#                 {% endif -%}
#                 {% endfor -%}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)
##########################################
#else
# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities -%}
#                 {% if c.id > 6 -%}
#                     <option value="{{c["id"]}}">{{c['city']}}</options>
#                 {% else -%}
#                     {{c['city']}}
#                 {% endif -%}
#                 {% endfor -%}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)
########################################
#elif
# cities = [  {'id' : 1, 'city' : 'Bishkek'},
#             {'id' : 21, 'city' : 'Orlovka'},
#             {'id' : 3, 'city' : 'Karakol'},
#             {'id' : 44, 'city' : 'Tokmok'},
#             {'id' : 156, 'city' : 'Osh'},]

# link =  '''  <select name='cities'>
#                 {% for c in cities -%}
#                 {% if c.id > 6 -%}
#                     <option value="{{c["id"]}}">{{c['city']}}</options>
#                 {% elif c.city == 'Bishkek' -%}
#                     <option>{{c['city']}}</option>
#                 {% else -%}
#                     {{c['city']}}
#                 {% endif -%}
#                 {% endfor -%}
#             </select>
#         '''

# tm = Template(link)
# msg = tm.render(cities=cities)

# print(msg)




#3 Фильтры и макросы macro, call
###################################
#sum - вычисление суммы поля коллекции
#sum(iterable,attribute=None,start=0)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]
# #attribute - это имменованный параметр
# tpl = "Суммарная цена автомобилей {{cs|sum(attribute='price')}}"
# tm = Template(tpl)
# msg = tm.render(cs = cars)

# print(msg)

#######################################

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]

# digs = [1,2,3,4,5]

# tpl = "Суммарная цена автомобилей {{cs|sum}}"
# tm = Template(tpl)
# msg = tm.render(cs = digs)

# print(msg)

#########################################
#max максимальное значение

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]

# tpl = "Суммарная цена автомобилей {{cs|max(attribute='price')}}"
# tm = Template(tpl)
# msg = tm.render(cs = cars)

# print(msg)  

#########################################
#max самая дорогая машина 
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]

# tpl = "Суммарная цена автомобилей {{ (cs|max(attribute='price')).model}}"
# tm = Template(tpl)
# msg = tm.render(cs = cars)

# print(msg) 

##########################################
# random
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]

# tpl = "Суммарная цена автомобилей {{ cs | random}}"
# tm = Template(tpl)
# msg = tm.render(cs = cars)

# print(msg) 
##########################################
# replace 
# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Scoda', 'price': 12000},
#     {'model': 'Volvo', 'price': 27500},
#     {'model': 'BMW', 'price': 13000},
# ]

# tpl = "Суммарная цена автомобилей {{ cs | replace('o', 'O')}}"
# tm = Template(tpl)
# msg = tm.render(cs = cars)

# print(msg) 

##########################################
#Можем применять фильтры внутри шаблона
#Блок filter
# {{%filter<название фильтра>%}}
#  <фрагмент для применения фильтра>
# {%endfilter%}

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
    
# ]

# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{%endfilter%}
# {% endfor -%}
# '''

# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)

##########################################
# Макроопределения

# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{type}}" name="{{name}}" value="{{value|e}}"size="{{size}}">
# {%- endmacro %}

# <p>{{input('username')}}
# <p>{{input('email')}}
# <p>{{input('password')}}
# '''

# tm = Template(html)
# msg = tm.render()
# print(msg)


##########################################
# Вложенные макросы -call
#{%call[(параметр)]<вызов макроса>%}
#<вложенный шаблон>
#{%endcall%}

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
# <li>{{u.name}}
# {%- endfor%}
# </ul>
# {%- endmacro %}

# {{list_users(users)}}
# '''

# tm = Template(html)
# msg = tm.render(users = persons)
# print(msg)

###########################################
# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# html = '''
# {% macro list_users(list_of_user) -%}
# <ul>
# {% for u in list_of_user -%}
# <li>{{u.name}}{{caller(u)}}
# {%- endfor%}
# </ul>
# {%- endmacro %}

# {% call(user) list_users(users) -%}
# <ul>
# <li>age: {{user.old}}
# <li>weight: {{user.weight}}
# </ul>
# {%- endcall %}
# '''

# tm = Template(html)
# msg = tm.render(users = persons)
# print(msg)

#############################################







#4 Загрузчики шаблонов - FileSystemLoader, PackageLoader, DictLoader, FunctionLoader

#Это пример предыдущих записей. Обычно они хранятся в отдельных файлах. 
# link = '''<select name="cities">
# {%for c in cities %}
#     <option value="{{c['id]}}">{{c['city']}}</option>
# {%endfor%}
# </select>'''
# Открываем main.html
##################################################
# PackageLoader
# from jinja2 import Environment, FileSystemLoader

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)

# tm = env.get_template('main.html')
# msg = tm.render(users = persons)

# print(msg)

#templates:
# PackageLoader - для загрузки шаблонов из пакета
# DictLoader - для загрузки шаблонов из словоря
# FunctionLoader - для загрузки на основе функции
# PrefixLoader - загрузчик, использующий словарь для построения подкаталогов 
# ChoiceLoader - загрузчик содержащий список других загрузчиков (если один не сработаетб выбирается следующий)
# ModuleLoader - загрузчик для скомпилированных шаблонов
###########################################################
# FunctionLoader
# from jinja2 import Environment, FunctionLoader

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# def loadTpl(path):
#     if path == 'index':
#         return '''Имя {{u.name}}, возраст {{u.old}}'''
#     else:
#         return '''Данные: {{u}}'''

# file_loader = FunctionLoader(loadTpl)
# env = Environment(loader=file_loader)

# tm = env.get_template('index')
# msg = tm.render(u = persons[0])

# print(msg)

############################################################








#5 Конструкции include и import
################################################################
#include
#Создаем html файлы - footer, header, page
# from jinja2 import Environment, FileSystemLoader

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)

# tm = env.get_template('page.html')
# msg = tm.render()

# print(msg)

##################################################
# from jinja2 import Environment, FileSystemLoader

# persons = [
#     {'name': 'Bolot', 'old': 16, 'weight': 78.5},
#     {'name': 'Akyl', 'old': 32, 'weight': 86.7},
#     {'name': 'Islam', 'old': 12, 'weight': 43},
# ]

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)

# tm = env.get_template('page.html')
# msg = tm.render(domain='http://itc.kg', title='Jinja')

# print(msg)









#6 Наследование и расширение шаблонов
###################################################
# {%block content %}
# {% endblock %}
# Создаем html файлы:
# ex_mail.html
# about.html
# from jinja2 import FileSystemLoader, Environment

# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)

# template = env.get_template('about.html')

# output = template.render()

# print(output)


# about.html
# {% extends 'layout/deffault.html' %}
# {% block title %}О сайте{% endblock %}
# {% block content %}
# {{super()}}
# <h1>{{self.title()}}</h1>
# <p>Классный сайт, если его доделать</p>
# {%endblock %}

#default.html
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{%block title %} {% endblock %}</title>
# </head>
# <body>
#     {% block content %}
#         Блок контента
#     {% endblock content %}
# </body>
# </html>