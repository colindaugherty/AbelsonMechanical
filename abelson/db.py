import sqlite3

db_file = 'abelson.sqlite'
user = ['username', 'password']

def make_dict(tup_list, fields):
    return [dict(zip(fields, d)) for d in tup_list]

def connect(db_file):
    db = sqlite3.connect(db_file)
    c = db.cursor()

    return (db, c)

def clean_up(db, c):
    c.close()
    db.close()

def get_user(username):
    db, c = connect()

    c.execute("SELECT * FROM user WHERE username=?", (username,))
    result = c.fetchone()
    result = make_dict(result, user)
    clean_up(db, c)

    return result

def new_job():
    db, c = connect()

    clean_up(db, c)

    pass

def update_job(job_data):
    db, c = connect()

    clean_up(db, c)

    return result

def get_job():
    db, c = connect()

    clean_up(db, c)

    return result

def update_loc(loc_data):
    db, c = connect()

    clean_up(db, c)

    return result

def get_loc():
    db, c = connect()

    clean_up(db, c)

    return result
