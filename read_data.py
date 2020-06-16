import matplotlib.pyplot as plt
import pandas as pd


def main():
    d = pd.read_csv('speed_records.csv', header=0, index_col=0, skipinitialspace=True, parse_dates=True)
    d.index = pd.DatetimeIndex(d.index)
    d.index = [d.index[i].replace(microsecond=0) for i in range(len(d))]
    d['download'].plot.bar(color='limegreen', title='Download')
    # _, ax = plt.subplots(nrows=2)
    # plt.tight_layout(rect=(0, 0.2, 1, 1))
    # ax[0].axes.xaxis.set_visible(False)
    # d['download'].plot.bar(ax=ax[0], color='limegreen', title='Download')
    # d['upload'].plot.bar(ax=ax[1], color='orange', title='Upload')
    plt.show()


if __name__ == '__main__':
    main()
