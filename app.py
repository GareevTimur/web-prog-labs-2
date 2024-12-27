from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/lab2/example")
def example():
    name = 'Тимур'
    return render_template('example.html', name=name)