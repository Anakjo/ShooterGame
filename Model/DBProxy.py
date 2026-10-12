import sqlite3

#Database proxy class to manage SQLite connections, table creation, and queries
class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        #Initialize the scores table if it doesn't already exist
        self.connection.execute('''
        CREATE TABLE IF NOT EXISTS dados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL, 
        score INTEGER NOT NULL, 
        date TEXT NOT NULL)
        '''
        )

    def save(self, score_dict: dict):
        #Insert a new player score record into the database and commit changes
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        #Fetch the top 10 highest scores ordered in descending order
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        #Safely close the database connection
        return self.connection.close()