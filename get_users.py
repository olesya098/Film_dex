from flask import Blueprint, jsonify

from db import get_connection

get_users_blueprint = Blueprint('get_users', __name__)

@get_users_blueprint.route('/api/v1/users')
def get_users():
    global conn, cur
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('SELECT * FROM user')

        users = cur.fetchall()

        users_json = []
        for user in users:
            users_json.append(
                {
                    'id': user[0],
                    'login': user[1],
                    'name': user[2],
                    'age': user[3],
                    'password': user[4]
                }
            )

        return jsonify(users_json)
    except:
        return jsonify({'message': 'error'})
    finally:
        cur.close()
        conn.close()