from pathlib import Path

import psycopg2

from app import config


class SQLite:
    def __init__(self):
        pass

    def __enter__(self):
        self.connection = psycopg2.connect(f'dbname={config["DB"]["DB_NAME"]} user={config["DB"]["USER"]}')
        return self.connection.cursor()

    def __exit__(self, *args):
        try:
            self.connection.commit()
        except:
            self.connection.rollback()
        finally:
            self.connection.close()

