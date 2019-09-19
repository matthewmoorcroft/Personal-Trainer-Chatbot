from connections.database import Database
# from model.plotter import plot_progress
from model.user_analysis import get_progress_info

# db = Database.get_instance()
# weights = db.get_weights(27)
# bodyfatratios = db.get_bodyfatratios('27')
# print(weights)

test_1 = {}
test_2 = {}

get_progress_info("27", "2", "Matt", "volume", "male", test_1, test_2)
# plot_progress('27', '375033117', weights, bodyfatratios)

# test = [85, None, None, None, None, None, None, None, None, None, None, 84]
#
# # print(next(pos, item for key, item in test if item is not None))
#
#
# value_i = None
# pos_i = None
#
# for pos, item in enumerate(test):
#     if item is not None:
#         value_i = item
#         pos_i = pos
#         break
#
#
# test.reverse()
#
# value_f = None
# pos_f = None
#
# for pos, item in enumerate(test):
#     if item is not None:
#         value_f = item
#         pos_f = pos
#         break
#
#
# pos_f = 12 - pos_f
#
# res = pos_f - pos_i
#
# rate = (value_f/value_i - 1) * 100
#
# print(rate)
