# -*- coding: utf-8 -*-
import datetime
import pandas as pd

def getNowdate():
    myday = datetime.datetime.now()
    dt = myday.strftime('%Y-%m-%d')
    return dt

def getYearQuarter(year,quarter):
    if year is None:
        year = datetime.datetime.now().year
    if quarter is None:
        month = datetime.datetime.now().month
        if month in [1, 2, 3]:
            quarter = 1
        elif month in [4, 5, 6]:
            quarter = 2
        elif month in [7, 8, 9]:
            quarter = 3
        else:
            quarter = 4
    return [year,quarter]

def getYearMonth(year,month):
    if year is None:
        year = datetime.datetime.now().year
    if month is None:
        month = datetime.datetime.now().month
    return [year,month]

def getStartTime(endTime =None,number = 1):
    if endTime is None:
        endTime = datetime.datetime.now()
        myday = endTime + datetime.timedelta(days=-number)
        endTime = endTime.strftime('%Y-%m-%d')
    else:
        myday =datetime.datetime.strptime(endTime, '%Y-%m-%d') + datetime.timedelta(days=-number)
    startTime = myday.strftime('%Y-%m-%d')
    return [startTime,endTime]

def getdatelist(beginTime, endTime):
    if endTime is None:
        endDate = datetime.datetime.now()
    else:
        endDate = datetime.datetime.strptime(endTime, '%Y-%m-%d')

    if beginTime is None:
        beginDate = endDate
    else:
        beginDate = datetime.datetime.strptime(beginTime, '%Y-%m-%d')

    date_l=[x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return date_l

if __name__ == '__main__':
    print getdatelist(None,None)