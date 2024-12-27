from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab2/example")
def example():
    name = 'Тимур'
    number = 2
    group = 'ФБИ-23'
    course = 3
    fruits = [
        {'name': 'манго', 'price': 100},
        {'name': 'арбузы', 'price': 120},
        {'name': 'бананы', 'price': 140},
        {'name': 'яблоки', 'price': 80}, 
        {'name': 'персики', 'price': 96}
    ]
    books = [
        {'author': 'Харлан Элисон','naming':'У меня нет рта, но я должен кричать', 'genre': 'постапокалиптика', 'pages': 10},
        {'author': 'Кормак Маккарти','naming':'Кровавый меридиан', 'genre': 'Вестерн', 'pages': 480},
        {'author': 'Дж. М. Кёсемен','naming':'Все грядущие дни', 'genre': 'Научная фантастика', 'pages': 308},
        {'author': 'Дж. К. Роулинг','naming':'Гарри Поттер и Кубок Огня', 'genre': 'Фэнтези, драма', 'pages': 704},
        {'author': 'Дрю Карпишин','naming':'Звёздные войны. Старая Республика: Реван', 'genre': 'Научная фантастика', 'pages': 298},
        {'author': 'Джордж Оруэлл','naming':'Скотный двор', 'genre': 'антиутопия, сатира', 'pages': 256},
        {'author': 'Джордж Оруэлл','naming':'1984', 'genre': 'антиутопия', 'pages': 320},
        {'author': 'Тимоти Зан','naming':'Траун', 'genre': 'Героическое зарубежное фэнтези ', 'pages': 480},
        {'author': 'Стивен Кинг','naming':'Кладбище Домашних животных', 'genre': 'Ужасы', 'pages': 373},
        {'author': 'Дж.Р.Р.Толкин','naming':'Сильмариллион', 'genre': 'Повесть', 'pages': 365}
    ]
    return render_template('example.html', name=name, number=number, group=group, course=course, fruits=fruits, books=books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2/lab2.html')