from logging import Logger
from sqlite3 import connect, Error

DB_FILENAME = 'db/tinny_etl.sqlite'
TABLE_SUFFIX = 'accounts'
INSERT_STATEMENT = '''INSERT OR REPLACE INTO {0}
                      VALUES (:game, :accountid, :gender, :age,
                      :country, :extract_date, :load_date)'''

CREATE_STATEMENT = '''CREATE TABLE IF NOT EXISTS {0}
                        (  game VARCHAR(3) NOT NULL,
                           accountid VARCHAR(255) NOT NULL PRIMARY KEY,
                           gender VARCHAR(6),
                           age INT,
                           country VARCHAR(255),
                           extract_date DATE NOT NULL,
                           load_date DATE NOT NULL
                        )'''


class Loader:

    def __init__(self, logger: Logger):
        self.logger = logger

    def load(self, data, game, db: str = DB_FILENAME):
        table_name = '{0}_{1}'.format(game, TABLE_SUFFIX)
        self.logger.info('Load data to {0} {1}'.format(table_name, db))

        with self.connect_to_db(db) as client:
            Loader.create_table(client, table_name)
            connection = client.cursor()
            prepare_statement = INSERT_STATEMENT.format(table_name)
            connection.executemany(prepare_statement, data)
            client.commit()

    def connect_to_db(self, db_filename: str):
        try:
            client = connect(db_filename)
            return client
        except Error as err:
            self.logger.error(
                'Connection to db {0} failed: {1}'.format(DB_FILENAME, err))
            return None

    @staticmethod
    def create_table(connection, table_name: str):
        prepare_statement = CREATE_STATEMENT.format(table_name)
        connection.execute(prepare_statement)
