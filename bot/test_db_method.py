from connections.database import Database
from model.plotter import plot_progress


db = Database.get_instance()
weights = db.get_weights('27')
bodyfatratios = db.get_bodyfatratios('27')
# print(weights)
plot_progress('27', '375033117', weights, bodyfatratios)
