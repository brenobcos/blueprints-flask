from app.models import DatabaseConnector

class User(DatabaseConnector):
    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.birthdate = kwargs["birthdate"]
        self.children = kwargs["children"]
        self.married = kwargs["married"]
        self.account_balance = kwargs["account_balance"]

    @classmethod
    def read_users(cls):
        #Cria os atributos conn e cur na classe Pai(DatabaseConector)
        cls.get_conn_cur()
        query = "SELECT * FROM users;"

        cls.cur.execute(query)

        users = cls.cur.fetchall()
        cls.cur.close()
        cls.conn.close()

        return users
