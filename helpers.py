from flask import redirect, render_template, request, session, g
from functools import wraps

import sqlite3

# Read and create a database based on a pure SQL file
def Database(path):
    # Create the database
    connection = sqlite3.connect('commerce.db', check_same_thread=False)
    cur = connection.cursor()

    # Addinng more sofistication and practicality
    connection.row_factory = sqlite3.Row

    # Read one line at a time from the file and when it matchs the end of a query, it is executed
    lines = []
    with open(path, "r") as f:
        for line in f:
            lines.append(line)
            # The ; marks the end of a query
            if ";" in line:
                # Join all strig into one query
                query = '\n'.join([line for line in lines])

                cur.execute(f"""{query}""")
                connection.commit()
                lines.clear()

# Allow operations in the database
def manipulatingData(query, array, response=False):
    with sqlite3.connect("commerce.db") as con:
        cur = con.cursor()
        cur.execute(f"""{query}""", array)
        res = cur.fetchall()

        # This way the database was not changed
        if response != False:
            return res
        # If response is not necessary, it means that problaby the database was changed     
        con.commit()

# Pages with this function can only be accessed if there is a user loged in
def login_required(f):
    """
    Decorate routes to require login.
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function