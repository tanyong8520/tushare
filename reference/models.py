# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# 参考数据

# 分配预案
class ProfitData(models.Model):
    date = models.DateField(u'日期')
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    year = models.FloatField(u'分配年份' )
    divi = models.FloatField(u'分红金额（每10股）')
    shares = models.FloatField(u'转增和送股数（每10股）' )

    def __unicode__(self):
        return '%s %s' % (self.date, self.code)

# 业绩预告
class ForecastData(models.Model):
    date = models.DateField(u'日期')
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    type = models.CharField(u'业绩变动类型【预增、预亏等】', max_length=50)
    report_date = models.FloatField(u'发布日期' )
    pre_eps = models.FloatField(u'上年同期每股收益')
    range = models.FloatField(u'业绩变动范围' )
    def __unicode__(self):
        return '%s %s' % (self.date, self.code)


# 限售股解禁
class XsgData(models.Model):
    date = models.DateField(u'日期')
    code = models.CharField(u'股票代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    ban_date = models.DateField(u'解禁日期')
    count = models.FloatField(u'解禁数量（万股）')
    ratio = models.FloatField(u'占总盘比率' )
    def __unicode__(self):
        return '%s %s' % (self.date, self.code)


# 基金持股
class FundDoldings(models.Model):
    date = models.DateField(u'日期')
    code = models.CharField(u'股票代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    report_date = models.DateField(u'报告日期')
    nums = models.FloatField(u'基金家数')
    nlast = models.FloatField(u'与上期相比（增加或减少了）' )
    count = models.FloatField(u'基金持股数（万股）')
    clast = models.FloatField(u'与上期相比')
    amount = models.FloatField(u'基金持股市值')
    ratio = models.FloatField(u'占流通盘比率')
    def __unicode__(self):
        return '%s %s' % (self.date, self.code)


# 新股数据
class NewStocks(models.Model):
    date = models.DateField(u'日期')
    code = models.CharField(u'股票代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    ipo_date = models.DateField(u'上网发行日期')
    issue_date = models.DateField(u'上市日期')
    amount = models.FloatField(u'发行数量(万股)')
    markets = models.FloatField(u'上网发行数量(万股)' )
    price = models.FloatField(u'发行价格(元)')
    pe = models.FloatField(u'发行市盈率')
    limit = models.FloatField(u'个人申购上限(万股)')
    funds = models.FloatField(u'募集资金(亿元)')
    ballot = models.FloatField(u'网上中签率(%)')
    def __unicode__(self):
        return '%s %s' % (self.date, self.code)

# 融资融券（沪市）
class ShMargins(models.Model):
    date = models.DateField(u'日期')
    opDate = models.DateField(u'信用交易日期')
    rzmre = models.FloatField(u'本日融资余额(元)')
    rqyl = models.FloatField(u'本日融券余量' )
    rqylje = models.FloatField(u'本日融券余量金额(元)')
    rqmcl = models.FloatField(u'本日融券卖出量')
    rzrqjyzl = models.FloatField(u'本日融资融券余额(元)')
    def __unicode__(self):
        return '%s' % (self.date)


# 融资融券明细数据
class ShMarginDetails(models.Model):
    date = models.DateField(u'日期')
    opDate = models.DateField(u'信用交易日期')
    stockCode = models.CharField(u'标的证券代码', max_length=50)
    securityAbbr = models.CharField(u'标的证券简称', max_length=50)
    rzye = models.FloatField(u'本日融资余额(元)')
    rzmre = models.FloatField(u'本日融资买入额(元)' )
    rzche = models.FloatField(u'本日融资偿还额(元)')
    rqyl = models.FloatField(u'本日融券余量')
    rqmcl = models.FloatField(u'本日融券卖出量')
    rqchl = models.FloatField(u'本日融券偿还量')
    def __unicode__(self):
        return '%s' % (self.date)

# 深市融资融券汇总数据
class SzMargins(models.Model):
    date = models.DateField(u'日期')
    opDate = models.DateField(u'信用交易日期')
    rzmre = models.FloatField(u'融资买入额(元)')
    rzye = models.FloatField(u'融资余额(元)' )
    rqmcl = models.FloatField(u'融券卖出量')
    rqyl = models.FloatField(u'融券余量')
    rqye = models.FloatField(u' 融券余量(元)')
    rzrqye = models.FloatField(u'融资融券余额(元)')
    def __unicode__(self):
        return '%s' % (self.date)


# 融资融券明细数据
class ShMarginDetails(models.Model):
    date = models.DateField(u'日期')
    opDate = models.DateField(u'信用交易日期')
    stockCode = models.CharField(u'标的证券代码', max_length=50)
    securityAbbr = models.CharField(u'标的证券简称', max_length=50)
    rzmre = models.FloatField(u'融资买入额(元))')
    rzye = models.FloatField(u'融资余额(元)' )
    rqmcl = models.FloatField(u' 融券卖出量')
    rqyl = models.FloatField(u'融券余量')
    rqye = models.FloatField(u'融券余量(元)')
    rzrqye = models.FloatField(u'融资融券余额(元)')
    def __unicode__(self):
        return '%s' % (self.date)