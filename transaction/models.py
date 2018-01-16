# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.db import models
#
# # 交易数据
import sqlalchemy.types as dbtype

from utilAll.Constants import *


class Transaction():
    baseType = {
# # 现金流量
# class HistData(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     open = models.FloatField(u'开盘价' )
#     high = models.FloatField(u'最高价' )
#     close = models.FloatField(u'收盘价' )
#     low = models.FloatField(u'最低价' )
#     volume = models.FloatField(u'成交量' )
#     price_change = models.FloatField(u'价格变动')
#     p_change = models.FloatField(u'涨跌幅')
#     ma5 = models.FloatField(u'5日均价')
#     ma10 = models.FloatField(u'10日均价')
#     ma20 = models.FloatField(u'20日均价')
#     v_ma5 = models.FloatField(u'5日均量')
#     v_ma10 = models.FloatField(u'10日均量')
#     v_ma20 = models.FloatField(u'20日均量')
#     turnover = models.FloatField(u'换手率')
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
        TRANSACTION_ALL_DATA: {
            'date': dbtype.TIMESTAMP(),
            'code': dbtype.CHAR(10),
            'open': dbtype.FLOAT(),
            'high': dbtype.FLOAT(),
            'close': dbtype.FLOAT(),
            'low': dbtype.FLOAT(),
            'volume': dbtype.FLOAT(),
            'amount': dbtype.FLOAT(),
        }
# # 复权历史数据
# class StockData(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     index = models.BooleanField(u'是否是大盘指数' )
#     open = models.FloatField(u'开盘价' )
#     high = models.FloatField(u'最高价' )
#     close = models.FloatField(u'收盘价' )
#     low = models.FloatField(u'最低价' )
#     volume = models.FloatField(u'成交量')
#     amount = models.FloatField(u'成交金额')
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
#
# # 事实行情数据
# class TodayAll(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     name = models.CharField(u'名称', max_length=50)
#     changepercent = models.FloatField(u'涨跌幅' )
#     trade = models.FloatField(u'现价' )
#     open = models.FloatField(u'开盘价' )
#     high = models.FloatField(u'最高价' )
#     low = models.FloatField(u'最低价')
#     settlement = models.FloatField(u'昨日收盘价')
#     volume = models.FloatField(u'成交量')
#     turnoverratio = models.FloatField(u'换手率')
#     amount = models.FloatField(u'成交量')
#     per = models.FloatField(u'市盈率')
#     pb = models.FloatField(u'市净率')
#     mktcap = models.FloatField(u'总市值')
#     nmc = models.FloatField(u'流通市值')
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
#
# # 历史分笔数据
# class TodayTicks(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     price = models.FloatField(u'成交价格' )
#     change = models.FloatField(u'价格变动' )
#     volume = models.FloatField(u'成交手')
#     amount = models.FloatField(u'成交金额(元)' )
#     type = models.CharField(u'买卖类型', max_length=50)
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
#
# # 大盘指数列表
# class AllIndex(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     change = models.FloatField(u'涨跌幅' )
#     open = models.FloatField(u'开盘点位' )
#     preclose = models.FloatField(u'昨日收盘点位')
#     close = models.FloatField(u'收盘点位' )
#     high = models.FloatField(u'最高点位' )
#     low = models.FloatField(u'最低点位' )
#     volume = models.FloatField(u'成交量(手)' )
#     amount = models.FloatField(u'成交金额（亿元）' )
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
#
# # 大单交易数据
# class SinaDd(models.Model):
#     date = models.DateField(u'日期')
#     code = models.CharField(u'代码', max_length=50)
#     name = models.CharField(u'名称', max_length=50)
#     price = models.FloatField(u'当前价格' )
#     volume = models.FloatField(u'成交手' )
#     preprice = models.FloatField(u'上一笔价格')
#     type = models.CharField(u'买卖类型', max_length=50)
#
#     def __unicode__(self):
#         return '%s %s' % (self.date, self.code)
    }