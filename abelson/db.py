import sqlite3

db_file = 'abelson.sqlite'
user = ['username', 'password']

def make_dict(tup_list, fields):
    return [dict(zip(fields, d)) for d in tup_list]

def connect():
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

def new_job(data):
    db, c = connect()
    c.execute('''INSERT INTO job (name, loc, description) VALUES (?, ?, ?)''',
              (data['name'], data['location'], data['description']))
    db.commit()
    clean_up(db, c)

    pass

# UPDATE users SET name=%s email=%s WHERE id=%s

def update_job(job_data):
    db, c = connect()

    db.commit()
    clean_up(db, c)

    pass

def get_job():
    db, c = connect()
    result = c.execute('''SELECT jb FROM job ORDER BY id''')
    clean_up(db, c)

    return result

def update_loc(loc_data):
    db, c = connect()

    db.commit()
    clean_up(db, c)

    pass

def get_loc():
    db, c = connect()
    c.execute('''SELECT * FROM loc ORDER BY id''')
    result = c.fetchall()
    clean_up(db, c)

    return result
