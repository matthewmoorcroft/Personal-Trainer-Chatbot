import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from datetime import date
from connections.net_manager import send_photo
import os
import pandas
# create data


def plot_progress(user_id, telegram_id, weights, bodyfatratios):

    # for row in data:

    period = np.array(range(1, 13))
    # weight = [84, 82, 81, 80, 79, 80, 80, 81, 82, 83, 83, 84]
    weight = [None, None, None, None, None, None, None, None, None, None, None, None]

    # bfr = [23, 22, 21, 20, 19, 19, 18, 18, 17, 16, 15, 14]
    bfr = [None, None, None, None, None, None, None, None, None, None, None, None]

    for key, item in weights.items():
        weight[int(key)-1] = float(item)

    for key, item in bodyfatratios.items():
        bfr[int(key)-1] = float(item)

    weight_filter = list(filter(None, weight))
    weight_min = int(min(weight_filter)/10)*10
    weight_max = int(max(weight_filter)/10+1)*10
    weight = np.array(weight).astype(np.double)
    # print(weight)
    weight_m = np.isfinite(weight)
    # print(weight_m)

    bfr_filtered = list(filter(None, bfr))
    bfr_min = int(min(bfr_filtered)/10)*10
    bfr_max = int(max(bfr_filtered)/10+1)*10
    bfr = np.array(bfr).astype(np.double)
    bfr_m = np.isfinite(bfr)

    fig, weight_p = plt.subplots()

    # plt.fill_between(period, weight, color="skyblue", alpha=0.3)

    color = 'tab:blue'
    weight_p.set_xlabel('2019')
    weight_p.set_ylabel('Weight (Kg)', color=color)

    weight_p.plot(period[weight_m], weight[weight_m], color=color, marker='o')
    weight_p.tick_params(axis='y', labelcolor=color)
    weight_p.axes.set_ylim([weight_min, weight_max])

    bfr_p = weight_p.twinx()  # instantiate a second axes that shares the same x-axis
    # plt.fill_between(period, bfr, color="red", alpha=0.3)
    color = 'tab:red'
    bfr_p.set_ylabel('Body Fat Ratio (%)', color=color)  # we already handled the x-label with ax1
    bfr_p.plot(period[bfr_m], bfr[bfr_m], color=color, marker='o')
    bfr_p.tick_params(axis='y', labelcolor=color)
    bfr_p.axes.set_ylim([bfr_min, bfr_max])

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    today = date.today()
    name = user_id+str(today)+".png"

    plt.savefig("resources/" + name)
    send_photo(name, telegram_id)
    os.remove("resources/" + name)
