import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# create data


def plot_image(data):

    # for row in data:

    period = range(1, 13)
    weight = [84, 82, 81, 80, 79, 80, 80, 81, 82, 83, 83, 84]
    bfr = [23, 22, 21, 20, 19, 19, 18, 18, 17, 16, 15, 14]

    weight_min = int(min(weight)/10)*10
    weight_max = int(max(weight)/10+1)*10

    bfr_min = int(min(bfr)/10)*10
    bfr_max = int(max(bfr)/10+1)*10

    fig, weight_p = plt.subplots()

    plt.fill_between(period, weight, color="skyblue", alpha=0.3)

    color = 'tab:blue'
    weight_p.set_xlabel('2019')
    weight_p.set_ylabel('Weight (Kg)', color=color)
    weight_p.plot(period, weight, color=color)
    weight_p.tick_params(axis='y', labelcolor=color)
    weight_p.axes.set_ylim([weight_min, weight_max])

    bfr_p = weight_p.twinx()  # instantiate a second axes that shares the same x-axis
    plt.fill_between(period, bfr, color="red", alpha=0.3)
    color = 'tab:red'
    bfr_p.set_ylabel('Body Fat Ratio (%)', color=color)  # we already handled the x-label with ax1
    bfr_p.plot(period, bfr, color=color)
    bfr_p.tick_params(axis='y', labelcolor=color)
    bfr_p.axes.set_ylim([bfr_min, bfr_max])

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()


plot_image(None)
