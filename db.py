import psycopg2
import settings


def get_rating(alias, db_conn):
    with db_conn.cursor() as curs:
        rating = curs.execute(f"SELECT * FROM racers WHERE alias = '{alias}'")
    return rating
