from flask import Blueprint, render_template, request, make_response, redirect, url_for
lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab3():
    return render_template('/lab3/lab3.html')