from yoyo import step

step(
    '''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(60) NOT NULL)''',
    '''DROP TABLE IF EXISTS user''',
)
