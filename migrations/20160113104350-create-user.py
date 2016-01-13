from yoyo import step

step(
    '''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL)''',
    '''DROP TABLE IF EXISTS user''',
)
