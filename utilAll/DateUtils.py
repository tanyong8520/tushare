# -*- coding: utf-8 -*-

from datetime import datetime

def getDateStr(date):
    return date.strftime("%Y-%m-%d")

def getDDayStr(d):
    return getDateStr(getDDate(datetime.date.today(),d))

def getDDate(date,d):
    dt=getDateTimeFromDate(date)
    dt=date+datetime.timedelta(days=1)*d
    return dt

def getDateTimeFromDate(date):
    return datetime.datetime(date.year,date.month,date.day)

# date 转 cron 表达式
def date2cron(year=None, month=None, day=None, hour=None, minute=None, week=None):
    date_arr = [minute, hour, day, month, week, year]
    for i, d in enumerate(date_arr):
        if not d:
            date_arr[i] = '*'
        else:
            if isinstance(d, tuple):
                d = ','.join(str(x) for x in d)
            elif isinstance(d, list):
                d = '-'.join(str(x) for x in d)
            date_arr[i] = str(d)
    expr = ' '.join(date_arr)
    return expr

# cron 转 date
def cron2date(exp):
    map = {}
    date_arr = ['second', 'minute', 'hour', 'day', 'month', 'week', 'year']
    exp = exp.replace('?','*')
    if isinstance(exp,str ):
        expList = exp.split(' ')
        for i,d in enumerate(date_arr):
            map[d] = expList[i]
    return map

# 获取当前时间
def getNowDate():
    return datetime.now()

def getToday():
    now=datetime.now()
    nowstr=now.strftime("%Y-%m-%d")
    return nowstr

if __name__ == '__main__':
    a = '2 0,24 0,5 * * ? '
    print cron2date(a)