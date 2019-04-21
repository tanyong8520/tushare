# -*- coding: utf-8 -*-

from strategy.base import *
from transaction.utils.TransactionInfo import TransactionInfo


def bankerOperation(data):
    ma_days = 10
    makeMAColumn(data, 'volume', ma_days)
    makeMAColumn(data, 'close', ma_days)
    operation_volume = 0
    operation_close = 0
    operation_volume = 0
    date_index = []
    number = 0;
    for index, row in data.iterrows():
        close_now_day = row['close']
        open_now_day = row['open']
        volume_now_day = row['volume']

        close_ma_5 = row["ma_close5"]
        volume_ma_5 = row["ma_volume5"]

        ratio = (close_now_day - open_now_day)/open_now_day
        # 振幅2%
        if -0.02 < ratio < 0.02:
            date_index.append(index)
            number = number+1

if __name__ == '__main__':
    stockData = TransactionInfo().getStockData("300369", "2018-01-01", "2019-01-01")
    nearData = stockData["2018-08-01": "2019-01-01"]
    makeRatio(nearData)
    ma_days = 5
    makeMAColumn(nearData, 'volume', ma_days)
    makeMAColumn(nearData, 'close', ma_days)

    print(nearData.tail(10))
    print(nearData.head(10))




