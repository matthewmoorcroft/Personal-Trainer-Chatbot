
class User:

    def __init__(self, telegram_id, id = -1, name = '', age = 0, gender = '', weight = 0, bodyfatratio = 0,
                 c_chest = 0, c_leg = 0, c_waist = 0, c_triceps = 0):

        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.telegram_id = telegram_id
        self.weight = weight
        self.bodyfatratio = bodyfatratio
        self.c_chest = c_chest
        self.c_leg = c_leg
        self.c_waist = c_waist
        self.c_triceps = c_triceps
