import sqlite3

db_file = 'abelson.sqlite'
USER = ['username', 'password']
JOBS = ['id', 'name', 'loc', 'description']
LOC = ['id', 'name', 'phone', 'fax', 'address', 'city', 'state', 'zipcode', 'email', "map"]

def make_dict(tup_list, fields):
    return [dict(zip(fields, d)) for d in tup_list]

def mapify_query_results(fields, results):
    output = []

    for result in results:
        entry = {}
        for i in range(len(fields)):
            entry[fields[i]] = result[i]
        output.append(entry)

    return output

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
    result = make_dict(result, USER)
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

def update_job(job_data, job_id):
    db, c = connect()
    c.execute('''UPDATE job SET name = ?, description = ?, loc = ? WHERE id == ?''',
              (job_data['name'], job_data['description'], job_data['location'], job_id))
    db.commit()
    clean_up(db, c)

    pass

def get_jobs():
    db, c = connect()
    c.execute('SELECT * FROM job')
    results = c.fetchall()
    results = mapify_query_results(JOBS, results)
    clean_up(db, c)

    return results

def get_job_by_id(job_id):
    db, c = connect()
    c.execute('SELECT * FROM job WHERE id == ?', (job_id,))
    results = c.fetchall()
    results = mapify_query_results(JOBS, results)
    clean_up(db, c)

    return results

def update_loc(loc_data):
    db, c = connect()
    c.execute('''UPDATE loc SET address = ?, city = ?, state = ?, zipcode = ?, fax = ?, phone = ?, email = ? WHERE id == ?''',
              (loc_data["address"], loc_data["city"], loc_data["state"], loc_data["zipcode"], loc_data["fax"], loc_data["phone"], loc_data["email"], loc_data["id"]))
    db.commit()
    clean_up(db, c)

    pass

def get_loc():
    db, c = connect()
    c.execute('''SELECT * FROM loc ORDER BY id''')
    result = c.fetchall()
    result = mapify_query_results(LOC, result)
    clean_up(db, c)

    return result
