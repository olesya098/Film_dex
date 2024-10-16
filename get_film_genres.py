from flask import Blueprint, jsonify

from db import get_connection

get_film_genres_blueprint = Blueprint('get_film_genres', __name__)

@get_film_genres_blueprint.route('/api/v1/genres_of_film/<int:film_id>')
def get_film_genres(film_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT genre_id FROM film_genre WHERE film_id={film_id}')

        film_genres = cur.fetchall()

        genres = []
        for film_genre in film_genres:
            genres.append(film_genre[0])

        return jsonify({'genres': genres})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()