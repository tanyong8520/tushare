# -*- coding: utf-8 -*-

from date2cron import *


# date 转 cron 表达式
def date2cron(year=None, month=None, day=None, hour=None, minute=None, week=None):
    return date_to_cron(year=None, month=None, day=None, hour=None, minute=None, week=None)

# cron 转 date
def cron2date(exp):
    map = {}
    date_arr = ['second', 'minute', 'hour', 'day', 'month', 'week', 'year']
    if isinstance(exp,str ):
        expList = exp.split(' ')
        for i,d in enumerate(date_arr):
            map[d] = expList[i]
    return map



if __name__ == '__main__':
    a = '2 0,24 0,5 * * ? '
    print cron2date(a)