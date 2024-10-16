from flask import Blueprint, jsonify

from db import get_connection

get_genres_blueprint = Blueprint('get_genres', __name__)

@get_genres_blueprint.route('/api/v1/genres')
def get_genres():
    global cur, conn
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM genre')

        genres = cur.fetchall()

        genres_json = []
        for genre in genres:
            genres_json.append(
                {
                    'id': genre[0],
                    'image': genre[1],
                    'title': genre[2]
                }
            )

        return jsonify(genres_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()