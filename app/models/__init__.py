import psycopg2
import os
from psycopg2 import sql

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
    def commit_and_close(cls, commit=True):
        if commit:
            cls.conn.commit()
        cls.conn.close()
        cls.cur.close()

    @classmethod
    def insert_into(cls, payload: dict, table_name: str):
        cls.get_conn_cur()

        sql_table_name = sql.Identifier(table_name)
        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                INSERT INTO {table}
                    ({columns})
                VALUES
                    ({values})
                RETURNING *
            """
        ).format(
            table=sql_table_name,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)

        result = cls.cur.fetchone()

        cls.commit_and_close()

        return result

    @classmethod
    def select_all(cls, table_name: str):
        cls.get_conn_cur()

        sql_table_name = sql.Identifier(table_name)

        query = sql.SQL(
            """
                SELECT * FROM {table}
            """
        ).format(table=sql_table_name)

        cls.cur.execute(query)

        result = cls.cur.fetchall()

        cls.commit_and_close()

        return result

    @classmethod
    def serialize(cls, values: tuple, columns: list[str]):
        return dict(zip(columns, values))
