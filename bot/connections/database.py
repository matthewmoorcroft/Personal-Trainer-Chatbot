import datetime
import psycopg2
import json
from model.logger import log


class Database:

    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                """dbname='pt'
                  user='matthew'
                  host='localhost'
                  password='1245788956'""")
        except psycopg2.Error:
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

            cur.execute("""SELECT *
                           FROM core.users
                           WHERE telegram_id = '%(telegram_id)s'  """, {
                'telegram_id': telegram_id
            })
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

                measurements = {
                    'weight': weight,
                    'bodyfatratio': bodyfatratio,
                    'c_chest': c_chest,
                    'c_leg': c_leg,
                    'c_waist': c_waist,
                    'c_triceps': c_triceps
                }
                user = {
                    'id': id,
                    'name': name,
                    'age': age,
                    'gender': gender,
                    'telegram_id': telegram_id,
                    'measurements': measurements
                }
                return user
            except Exception as e:
                log(e, 'LOG_ERROR')
                return None
                # cache.add_user2cache(user)

    def add_user(self, user):

        name = user['name']
        age = user['age']
        gender = user['gender']
        telegram_id = user['telegram_id']
        weight = user['measurements']['weight']
        bodyfatratio = user['measurements']['bodyfatratio']
        c_chest = user['measurements']['c_chest']
        c_leg = user['measurements']['c_leg']
        c_waist = user['measurements']['c_waist']
        c_triceps = user['measurements']['c_triceps']

        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO core.users (name,
                                                   age,
                                                   gender,
                                                   telegram_id,
                                                   weight,
                                                   bodyfatratio,
                                                   c_chest,
                                                   c_leg,
                                                   c_waist,
                                                   c_triceps)
                        VALUES (%(name)s,
                               %(age)s,
                               %(gender)s,
                               %(telegram_id)s,
                               %(weight)s,
                               %(bodyfatratio)s,
                               %(c_chest)s,
                               %(c_leg)s,
                               %(c_waist)s,
                               %(c_triceps)s)""", {
                'name': name,
                'age': age,
                'gender': gender,
                'telegram_id': telegram_id,
                'weight': weight,
                'bodyfatratio': bodyfatratio,
                'c_chest': c_chest,
                'c_leg': c_leg,
                'c_waist': c_waist,
                'c_triceps': c_triceps})
            self.conn.commit()
            cur.close()
            return json.dumps({'result': "ok"})
        except Exception as e:

            print(e)
            return json.dumps({'result': "Error: Not all fields filled"})

    def delete_user(self, user_id):

        cur = self.conn.cursor()

        cur.execute("""DELETE FROM core.users
                       WHERE id = %(user_id)s""", {'user_id': user_id})

        self.database.conn.commit()
        response = {'result': 'ok'}
        return response

    def get_message(self, uid):
        cur = self.conn.cursor()

        cur.execute("""UPDATE webhook.incoming_messages
                       SET assigned_to='%(uid)s'
                       WHERE id = (SELECT id
                                   FROM webhook.incoming_messages
                                   WHERE source='Telegram'
                                   AND assigned_to IS null LIMIT 1)""")

        self.conn.commit()

        cur.execute("""SELECT id, message
                       FROM webhook.incoming_messages
                       WHERE assigned_to='%(uid)s'
                       AND processed_on IS null LIMIT 1""", {'uid': uid})

        rows = cur.fetchall()
        rowcount = cur.rowcount

        if rowcount:

            for row in rows:
                row_id = row[0]
                raw_message = json.loads(row[1])['message']
                return row_id, raw_message
        return None

    def add_log(self, message, intent, id_to='Sam', id_from='Sam', score=-1):
        cur = self.conn.cursor()
        cur.execute(
            """INSERT INTO core.interaction_log (
                            id_to,
                            id_from,
                            message,
                            intent,
                            score) VALUES (%(id_to)s,
                                           %(id_from)s,
                                           %(message)s,
                                           %(intent)s,
                                           %(score)s)""", {
                'id_to': id_to,
                'id_from': id_from,
                'message': message,
                'intent': intent,
                'score': score
            })
        self.conn.commit()
        cur.close()

    def update_processes(self, row_id):
        cur = self.conn.cursor()

        cur.execute("""UPDATE webhook.incoming_messages
                       SET processed_on='%(date)s'
                       WHERE id=%(row_id)s""", {
            'date': datetime.datetime.now(),
            'row_id': row_id
        })
        self.conn.commit()
        cur.close()
