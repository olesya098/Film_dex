from flask import Blueprint, jsonify

from db import get_connection

get_films_blueprint = Blueprint('get_films', __name__)


@get_films_blueprint.route('/api/v1/films', methods=['GET'])
def get_films():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM film')

        films = cur.fetchall()

        films_json = []
        for film in films:
            cur.execute(f'SELECT title FROM Category_film WHERE Category_film_id={film[7]}')
            category_film = cur.fetchone()[0]

            films_json.append(
                {
                    'id': film[0],
                    'image': film[1],
                    'title': film[2],
                    'rate': film[3],
                    'age': film[4],
                    'year': film[5],
                    'country': film[6],
                    'category_film': category_film,
                    'description': film[8],
                    'link': film[9],
                    'category': film[10]
                }
            )

        return jsonify(films_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()


@get_films_blueprint.route('/api/v1/films/<int:film_id>', methods=['GET'])
def get_film(film_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT * FROM film WHERE film_id={film_id}')

        film = cur.fetchone()

        cur.execute(f'SELECT title FROM Category_film WHERE Category_film_id={film[7]}')
        category_film = cur.fetchone()[0]

        film_json = {
            'id': film[0],
            'image': film[1],
            'title': film[2],
            'rate': film[3],
            'age': film[4],
            'year': film[5],
            'country': film[6],
            'category_film': category_film,
            'description': film[8],
            'link': film[9],
            'category': film[10]
        }

        return jsonify(film_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()
