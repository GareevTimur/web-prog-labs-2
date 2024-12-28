from flask import Blueprint, render_template, request, current_app
lab7 = Blueprint('lab7',  __name__ ) 

@lab7.route('/lab7/') 
def main(): 
    return render_template('lab7/index.html') 

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film(): 
    film = request.get_json()

    errors, film = check(film)
    if errors:
        return errors, 400

    #films.append(film)  
    insertFilm(film)
    return "Success", 201