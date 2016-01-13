from yoyo import step

step(
    '''CREATE TABLE IF NOT EXISTS loc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE NOT NULL,
        map UNIQUE NOT NULL,
        phone INTEGER UNIQUE NOT NULL,
        fax INTEGER UNIQUE NOT NULL,
        address TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL)''',
    '''DROP TABLE IF EXISTS loc''',
)
