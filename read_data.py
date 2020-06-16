import matplotlib.pyplot as plt
import pandas as pd


def plot(column_name='download'):  # or 'upload'
    # /19143857/pandas-bar-plot-xtick-frequency
    d = pd.read_csv('speed_records.csv', header=0, index_col=0, skipinitialspace=True, parse_dates=True)
    d.index = pd.DatetimeIndex(d.index)
    d.index = [d.index[i].replace(microsecond=0) for i in range(len(d))]

    n = 5
    avg = d[column_name].mean()
    time_delta = str(d.index[-1] - d.index[0])
    color = 'limegreen' if column_name == 'download' else 'gold'
    ax = d[column_name].plot.bar(color=color, title=f'{column_name.title()} - AVG: {avg:.3f} Mbit/s ({time_delta})')
    # ax.grid(True)
    ticks = ax.xaxis.get_ticklocs()
    ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
    ax.xaxis.set_ticks(ticks[::n])
    ax.xaxis.set_ticklabels(ticklabels[::n])
    ax.figure.show()
    # _, ax = plt.subplots(nrows=2)
    # plt.tight_layout(rect=(0, 0.2, 1, 1))
    # ax[0].axes.xaxis.set_visible(False)
    # d['download'].plot.bar(ax=ax[0], color='limegreen', title='Download')
    # d['upload'].plot.bar(ax=ax[1], color='orange', title='Upload')
    plt.show()


def main():
    plot('download')
    plot('upload')


if __name__ == '__main__':
    main()
