# -*- coding: utf-8 -*-

import talib as tl
from talib import MA_Type
import pandas as pd
import logging

def makeMAColumn(data, indicators = 'cloes', ma_days = 5):
    '''计算指定天数的指定指标的平均线,默认计算收盘价格'''
    ma_tag = 'ma' +'_' + indicators + str(ma_days)
    data[ma_tag] = pd.Series(tl.MA(data[indicators].values, ma_days), index=data.index.values)

def makeBBANDSColumn(data, indicators = 'cloes'):
    '''计算指定指标的布林带,默认计算收盘价格
    中间线 = 20 日均线
    Up 线 = 20 日均线 + 2SD（20 日收巿价）
    Down 线 =20 日均线 - 2SD（20 日收巿价)
    20 日收巿价的标准差 SD'''
    ma_tag = 'bbands' + '_' + +indicators
    upper, middle, lower = tl.BBANDS(data[indicators].values, matype=MA_Type.T3)
    data[ma_tag+'upper'] = pd.Series(upper, index=data.index.values)
    data[ma_tag+'middle'] = pd.Series(middle, index=data.index.values)
    data[ma_tag + 'lower'] = pd.Series(lower, index=data.index.values)

def makeRatio(data):
    data.eval('ratio = (close - open)/open *100', inplace=True)


