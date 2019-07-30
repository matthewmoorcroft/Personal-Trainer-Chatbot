import datetime
import psycopg2
import json
from model.logger import log, LogTypes
import traceback


class Database:

    instance = None

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                """dbname='pt'
                  user='matthewmoorcroft'
                  host='localhost'
                  password='1245788956'""")
        except psycopg2.Error:
            print("ERROR: Unable to connect to the database")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Database()
        return cls.instance

    def get_user_id(self, telegram_id):
        try:
            cur = self.conn.cursor()

            cur.execute("""SELECT id
                           FROM core.users
                           WHERE telegram_id = %(telegram_id)s
                            """, {
                'telegram_id': telegram_id
            })

            row = cur.fetchone()

            if cur.rowcount == 0:
                cur.close()
                return 0
            else:
                cur.close()
                return row[0]

        except Exception as e:

            print(e)
            return 0

    def check_user_exists(self, telegram_id):
        try:
            cur = self.conn.cursor()

            cur.execute("""SELECT id,
                                  user_name,
                                  user_gender,
                                  measure_user
                           FROM core.users
                           WHERE telegram_id = %(telegram_id)s
                            """, {
                'telegram_id': telegram_id
            })

            # Local
            return True, "1", "Test", "male", True
            # return False, 0, None, None, False
            ##
            row = cur.fetchone()

            if cur.rowcount == 0:
                cur.close()

                return False, "0", None, None, False
            else:
                cur.close()
                return True, row[0], row[1], row[2], row[3]

        except Exception as e:

            print(e)
            return False, 0, None, None, False

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
            cur.close()
        except Exception as e:

            print(e)

        try:
            # for row in rows:
            id = rows[0][0]
            name = rows[0][1]
            age = rows[0][2]
            gender = rows[0][3]
            telegram_id = rows[0][4]
            weight = rows[0][5]
            bodyfatratio = rows[0][6]
            c_chest = rows[0][7]
            c_leg = rows[0][8]
            c_waist = rows[0][9]
            c_triceps = rows[0][10]

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
            log(str(e), LogTypes.LOG_ERROR)
            return {'result': "ERROR"}
            # cache.add_user2cache(user)

    def add_user(self, telegram_id, user_name, birthdate, user_gender, training_type, measure_user):

        try:
            cur = self.conn.cursor()

            cur.execute("""INSERT INTO core.users (user_name,
                                                   birthdate,
                                                   user_gender,
                                                   telegram_id,
                                                   training_type,
                                                   measure_user)
                        VALUES (%(user_name)s,
                               %(birthdate)s,
                               %(user_gender)s,
                               %(telegram_id)s,
                               %(training_type)s,
                               %(measure_user)s)""", {
                'user_name': user_name,
                'birthdate': birthdate,
                'user_gender': user_gender,
                'telegram_id': telegram_id,
                'training_type': training_type,
                'measure_user': measure_user})
            self.conn.commit()
            cur.close()
            return json.dumps({'result': "ok"})
        except Exception as e:
            self.conn.rollback()
            cur.close()

            print(e)
            return json.dumps({'result': "Error: Failed to add user"})

    def add_measurements(self, user_id, weight, bodyfatratio):

        try:
            cur = self.conn.cursor()

            cur.execute("""SELECT *
                           FROM core.weights
                           WHERE measurement_date = CURRENT_DATE AND user_id = %(user_id)s
                            """, {
                'user_id': user_id
            })
            if cur.rowcount == 0:
                cur.execute("""INSERT INTO core.weights
                               (user_id, weight)
                               VALUES(%(user_id)s, %(weight)s);
                                """, {
                    'user_id': user_id,
                    'weight': weight
                })
            else:
                cur.execute("""UPDATE core.weights
                               SET weight = %(weight)s
                               WHERE measurement_date = CURRENT_DATE
                               AND user_id = %(user_id)s
                                """, {
                    'user_id': user_id,
                    'weight': weight
                })

            self.conn.commit()
            cur.execute("""SELECT *
                           FROM core.bodyfatratio
                           WHERE measurement_date = CURRENT_DATE
                           AND user_id = %(user_id)s
                            """, {
                'user_id': user_id
            })
            if cur.rowcount == 0:
                cur.execute("""INSERT INTO core.bodyfatratio
                               (user_id, bodyfatratio)
                               VALUES(%(user_id)s, %(bodyfatratio)s);
                                """, {
                    'user_id': user_id,
                    'bodyfatratio': bodyfatratio
                })
            else:
                cur.execute("""UPDATE core.bodyfatratio
                               SET bodyfatratio = %(bodyfatratio)s
                               WHERE measurement_date = CURRENT_DATE
                               AND user_id = %(user_id)s
                                """, {
                    'user_id': user_id,
                    'bodyfatratio': bodyfatratio
                })
            self.conn.commit()
            cur.execute("""UPDATE core.measurements
                           SET bodyfatratio = %(bodyfatratio)s, weight = %(weight)s
                           WHERE user_id = %(user_id)s
                            """, {
                'user_id': user_id,
                'bodyfatratio': bodyfatratio,
                'weight': weight
            })
            self.conn.commit()
            cur.close()
            return json.dumps({'result': "ok"})
        except Exception as e:
            self.conn.rollback()
            cur.close()
            print(e)
            return json.dumps({'result': "Error: Failed to add measurements"})

    def delete_user(self, user_id):

        cur = self.conn.cursor()

        cur.execute("""DELETE FROM core.users
                       WHERE id = %(user_id)s""", {'user_id': user_id})

        self.database.conn.commit()
        cur.close()
        response = {'result': 'ok'}
        return response

    def get_message(self, uid):
        cur = self.conn.cursor()

        cur.execute("""UPDATE webhook.incoming_messages
                       SET assigned_to=%(uid)s
                       WHERE id = (SELECT id
                                   FROM webhook.incoming_messages
                                   WHERE source='Telegram'
                                   AND assigned_to IS null LIMIT 1)""",
                    {'uid': uid})

        self.conn.commit()

        cur.execute("""SELECT id, message
                       FROM webhook.incoming_messages
                       WHERE assigned_to=%(uid)s
                       AND processed_on IS null LIMIT 1""", {'uid': uid})

        rows = cur.fetchall()
        rowcount = cur.rowcount

        cur.close()
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

    def update_processed(self, row_id):
        cur = self.conn.cursor()

        cur.execute("""UPDATE webhook.incoming_messages
                       SET processed_on=%(date)s
                       WHERE id=%(row_id)s""", {
            'date': datetime.datetime.now(),
            'row_id': row_id
        })
        self.conn.commit()
        cur.close()
