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
    return render_template('example.html', name=name, number=number, group=group, course=course)