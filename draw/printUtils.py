import matplotlib.pyplot as plt
import mpl_finance as mpf
import datetime
from matplotlib.pylab import date2num

def makeAll(hist_date):
    rect1 = [0.02, 0.48, 0.98, 0.5]
    rect2 = [0.02, 0.35, 0.98, 0.1]
    rect3 = [0.02, 0.08, 0.98, 0.20]
    plt.figure(figsize=(18, 15),frameon =False)
    ax1 = plt.axes(rect1)
    makeStockKLine(ax1, hist_date)

    ax2 = plt.axes(rect2)
    makeVolume(ax2, hist_date)

    ax3 = plt.axes(rect3)
    makeOther(ax3, hist_date)

    plt.ylabel("Price")
    plt.show()

def makeHist(ax, hist_date):
    kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)
    for column in hist_date:
        if column in ['close','open']:
            ax.hist(hist_date[column], kwargs)


def makeOther(ax, hist_data):
    for column in hist_data:
        if column in ['close','high','volume']: #'low','open'
            continue
        ax.plot(hist_data.index, hist_data[column], label=column)
    length = len(hist_data)
    xticks = list(range(0, length, length/20))
    xlabels = [hist_data.index[x] for x in xticks]
    xticks.append(len(hist_data.index))
    xlabels.append(hist_data.index[-1])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation=40)

def makeVolume(ax, hist_data):
    ax.set_title("Volume")
    ax.plot(hist_data.index, hist_data['volume'])
    length = len(hist_data)
    xticks = list(range(0, length, length / 20))
    xlabels = [hist_data.index[x] for x in xticks]
    xticks.append(len(hist_data.index))
    xlabels.append(hist_data.index[-1])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, rotation=40)


def makeStockKLine(ax, hist_data):
    if type(hist_data)==type(None):
        return;
    data_list = []
    for dates, row in hist_data.iterrows():
        if type(dates) == str:
            date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
        else:
            date_time = dates
        t = date2num(date_time)
        close, high, low, open = row[:4]
        datas = (t, open, high, low, close)
        data_list.append(datas)

    ax.xaxis_date()
    ax.set_title("K_Line")
    # ax.xticks(rotation=45)
    # ax.yticks()
    # ax.xlabel("Time")
    # ax.ylabel("Price")
    mpf.candlestick_ohlc(ax, data_list, width=1, colorup='r', colordown='green')
    print("grid");