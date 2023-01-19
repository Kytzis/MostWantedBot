import psycopg2
import settings


db_conn = psycopg2.connect(
    database = settings["db_name"],
    host = settings["db_host"],
    port = settings["db_port"],
    user = settings["db_user"],
    password = settings["db_password"]
)
db_cursor = db_conn.cursor()

db_cursor.execute("CREATE TABLE racers(alias text, rating int)")