import db


def handle_response(message, db_conn):
    p_message = message.lower().split(" ")

    # Get rating of a single racer
    if p_message[0] == "getrating":
        if len(p_message) < 2 or p_message[1] == "":
            return "Invalid use of GetRating, please provide a racing alias."
        return db.get_rating(p_message[1], db_conn)
