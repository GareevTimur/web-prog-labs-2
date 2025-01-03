from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab6)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Гареев Тимур Артурович, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <h2>Меню</h2>
        <ul>
        <li><a href = "/lab1">1 лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab2">2 лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab3">3 лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab4">4 лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab5">5 лабораторная</a></li>
        </ul>
        <ul>
        <li><a href = "/lab6">6 лабораторная</a></li>
        </ul>

        <footer>
            &copy; Гареев Тимур, ФБИ-23, 3 курс, 2024
        </footer>
    </body>
</html>
"""