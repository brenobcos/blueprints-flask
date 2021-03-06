from turtle import update
from app.models import DatabaseConnector
from psycopg2 import sql


class User(DatabaseConnector):

    table_name = "users"

    # user_columns = [
    #     "_id",
    #     "email",
    #     "birthdate",
    #     "children",
    #     "married",
    #     "account_balance",
    # ]

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    # @classmethod
    # def serialize(cls, data: tuple):
    #     return dict(zip(cls.user_columns, data))

    @classmethod
    def select_all(cls):
        return super().select_all(cls.table_name)

    # @classmethod
    # def read_users(cls):
    #     # Cria os atributos conn e cur na classe Pai(DatabaseConector)
    #     cls.get_conn_cur()
    #     query = "SELECT * FROM users;"

    #     cls.cur.execute(query)

    #     users = cls.cur.fetchall()
    #     cls.cur.close()
    #     cls.conn.close()

    #     return users

    # def create_user(self):

    #     self.get_conn_cur()

    #     query = """
    #         INSERT INTO users
    #             (email, birthdate, children, married, account_balance)
    #         VALUES
    #             (%s,%s,%s,%s,%s)
    #         RETURNING * 
    #     """

    #     query_values = tuple(self.__dict__.values())

    #     self.cur.execute(query, query_values)

    #     self.conn.commit()

    #     inserted_user = self.cur.fetchone()

    #     self.cur.close()
    #     self.conn.close()

    #     return inserted_user

    def insert_into(self):
        return super().insert_into(self.__dict__, self.table_name)


    @classmethod
    def update_user(cls, user_id: str, payload: dict):
        cls.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        sql_user_id = sql.Literal(user_id)

        query = sql.SQL(
            """
                UPDATE
                    users
                SET
                    ({columns}) = ROW({values})
                WHERE
                    id={id}
                RETURNING *;            
            """
        ).format(
            id=sql_user_id,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)

        update_user = cls.cur.fetchone()

        cls.commit_and_close()

        return update_user
