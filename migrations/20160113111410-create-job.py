from yoyo import step

step(
    '''CREATE TABLE IF NOT EXISTS job (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        loc INTEGER NOT NULL,
        description TEXT NOT NULL
    )''',
    '''DROP TABLE IF EXISTS job''',
)
