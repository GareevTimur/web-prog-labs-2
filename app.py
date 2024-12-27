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
    return render_template('example.html', name=name, number=number, group=group, course=course, fruits=fruits)