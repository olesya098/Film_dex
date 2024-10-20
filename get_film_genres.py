from flask import Blueprint, jsonify

from db import get_connection

get_film_genres_blueprint = Blueprint('get_film_genres', name)

@get_film_genres_blueprint.route('/api/v1/film_with_genre/<int:genre_id>')
def get_film_genres(genre_id):
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f'SELECT film_id FROM film_genre WHERE genre_id={genre_id}')

        film_genres = cur.fetchall()

        films = []
        for film_genre in film_genres:
            films.append(film_genre[0])

        return jsonify({'films': films})
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()