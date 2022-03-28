import psycopg2
import os

configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

conn = psycopg2.connect(**configs)

class DatabaseConnector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()

    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.conn.close()
        cls.cur.close()
