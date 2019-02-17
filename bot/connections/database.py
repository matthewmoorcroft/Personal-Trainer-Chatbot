from model.user import User
import datetime
import psycopg2
import json


class Database:

    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                "dbname='pt' user='matthew' host='localhost' password='1245788956'")
        except:
            print("ERROR: Unable to connect to the database")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database()
        return cls.instance

    def check_user(self, telegram_id):

        # user = cache.check_user()

        # if user is not None:
        #     return user

        try:
            cur = self.conn.cursor()

            cur.execute("""SELECT * FROM core.users
                        WHERE telegram_id = '{telegram_id}'  """)
            rows = cur.fetchall()

        except Exception as e:

            print(e)
        else:

            try:
                for row in rows:
                    id = row[0]
                    name = row[1]
                    age = row[2]
                    gender = row[3]
                    telegram_id = row[4]
                    weight = row[5]
                    bodyfatratio = row[6]
                    c_chest = row[7]
                    c_leg = row[8]
                    c_waist = row[9]
                    c_triceps = row[10]

                user = User(id, name, age, gender, telegram_id, weight,
                            bodyfatratio, c_chest, c_leg, c_waist, c_triceps)
                return user
            except:
                return None
                # cache.add_user2cache(user)

    def add_user(self, telegram_id):

        user = cache.check_user()

        if user is not None:
            return user

        try:
            cur = self.conn.cursor()

            cur.execute("""SELECT * FROM core.users
                        WHERE telegram_id = '{telegram_id}'  """)
            rows = cur.fetchall()

        except Exception as e:

            print(e)
        else:

            try:
                for row in rows:
                    id = row[0]
                    name = row[1]
                    age = row[2]
                    gender = row[3]
                    telegram_id = row[4]
                    weight = row[5]
                    bodyfatratio = row[6]
                    c_chest = row[7]
                    c_leg = row[8]
                    c_waist = row[9]
                    c_triceps = row[10]

                user = User(id, name, age, gender, telegram_id, weight,
                            bodyfatratio, c_chest, c_leg, c_waist, c_triceps)
                return user
            except:
                return None
                # cache.add_user2cache(user)

    def delete_user(self, telegram_id):

        user = cache.check_user()

        if user is not None:
            return user

        try:
            cur = self.conn.cursor()

            cur.execute('SELECT * FROM core.users WHERE telegram_id = ' + telegram_id)
            rows = cur.fetchall()

        except:

            print("Error executing query")
        else:

            try:
                for row in rows:
                    id = row[0]
                    name = row[1]
                    age = row[2]
                    gender = row[3]
                    telegram_id = row[4]
                    weight = row[5]
                    bodyfatratio = row[6]
                    c_chest = row[7]
                    c_leg = row[8]
                    c_waist = row[9]
                    c_triceps = row[10]

                user = User(id, name, age, gender, telegram_id, weight,
                            bodyfatratio, c_chest, c_leg, c_waist, c_triceps)
                return user
            except:
                return None
                # cache.add_user2cache(user)

    def get_message(self, uid):
        cur = self.conn.cursor()

        cur.execute("UPDATE webhook.incoming_messages set assigned_to='" + uid +
                    "' where id = (SELECT id FROM webhook.incoming_messages where source='Telegram' and assigned_to is null LIMIT 1)")

        self.conn.commit()

        cur.execute("SELECT id, message from webhook.incoming_messages where assigned_to='" +
                    uid + "' and processed_on is null LIMIT 1")

        rows = cur.fetchall()
        rowcount = cur.rowcount

        if rowcount:

            for row in rows:
                row_id = row[0]
                raw_message = json.loads(row[1])['message']
                return row_id, raw_message
        return None

    def add_log(self, message, intent, id_to='Sam', id_from='Sam', score=-1):
        db.update_processed(row_id)
        cur.execute(
            "INSERT INTO core.interaction_log (id_to, id_from, message, intent, score) VALUES ('{id_to}','{id_from}','{message}','{intent}',{score})")
        conn.commit()
        cur.close()

    def update_processes(self, row_id):
        db.update_processed(row_id)
        cur.execute("UPDATE webhook.incoming_messages SET processed_on='" +
                    str(datetime.datetime.now()) + "' where id='" + str(row_id) + "'")
        conn.commit()
        cur.close()
