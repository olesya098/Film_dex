import sqlite3


def get_connection():
    conn = sqlite3.connect('FilmDex.db')

    return conn