from connections.database import Database


class User:

    def __init__(self,
                 telegram_id,
                 id=None,
                 name=None,
                 age=None,
                 gender=None,
                 weight=0,
                 bodyfatratio=0,
                 c_chest=0,
                 c_leg=0,
                 c_waist=0,
                 c_triceps=0):

        db = Database.get_instance()

        user = db.check_user(telegram_id)

        # try:

        self.id = user['id']
        self.name = user['name']
        self.age = user['age']
        self.gender = user['gender']
        self.telegram_id = user['telegram_id']
        self.weight = user['measurements']['weight']
        self.bodyfatratio = user['measurements']['bodyfatratio']
        self.c_chest = user['measurements']['c_chest']
        self.c_leg = user['measurements']['c_leg']
        self.c_waist = user['measurements']['c_waist']
        self.c_triceps = user['measurements']['c_triceps']

        # except:
            # self.telegram_id = telegram_id
            # log()
