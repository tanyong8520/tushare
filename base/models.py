# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# 基本面
class Company(models.Model):
    full_name = models.CharField(u'公司全称', max_length=50)
    address = models.CharField(u'地址', max_length=200)
    tel = models.CharField(u'电话', max_length=15, blank=True)

    def __unicode__(self):
        return '%s %s %s' % (self.full_name, self.address, self.tel)


# 股票列表
class StockBasics(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    industry = models.CharField(u'所属行业', max_length=50)
    area = models.CharField(u'地区', max_length=20)
    pe = models.FloatField(u'市盈率')
    outstanding = models.FloatField(u'流通股本(亿)' )
    totals = models.FloatField(u'总股本(亿)' )
    totalAssets = models.FloatField(u'总资产(万)' )
    liquidAssets = models.FloatField(u'流动资产' )
    fixedAssets = models.FloatField(u'固定资产' )
    reserved = models.FloatField(u'公积金' )
    reservedPerShare= models.FloatField(u'每股公积金' )
    esp= models.FloatField(u'每股收益' )
    bvps = models.FloatField(u'每股净资' )
    pb = models.FloatField(u'市净率' )
    timeToMarket = models.CharField(u'上市日期', max_length=20)
    undp = models.FloatField(u'未分利润' )
    perundp = models.FloatField(u'每股未分配' )
    rev = models.FloatField(u'收入同比(%)' )
    profit = models.FloatField(u'利润同比(%)' )
    gpr = models.FloatField(u'毛利率(%)' )
    npr = models.FloatField(u'净利润率(%)' )
    holders = models.FloatField(u'股东人数' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.industry)

# 业绩报告
class ReportData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    esp = models.FloatField(u'每股收益' )
    eps_yoy = models.FloatField(u'每股收益同比( %)' )
    bvps = models.FloatField(u'每股净资产' )
    roe = models.FloatField(u'净资产收益率( %)' )
    epcf = models.FloatField(u'每股现金流量(元)' )
    net_profits = models.FloatField(u'净利润(万元)' )
    profits_yoy = models.FloatField(u'净利润同比( %)' )
    distrib = models.FloatField(u'分配方案' )
    report_date = models.CharField(u'发布日期', max_length=20)

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.esp)

# 盈利能力
class ProfitData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    roe = models.FloatField(u'净资产收益率(%)' )
    net_profit_ratio = models.FloatField(u'净利率(%)' )
    gross_profit_rate = models.FloatField(u'毛利率(%)' )
    net_profits = models.FloatField(u'净利润(万元)' )
    esp = models.FloatField(u'每股收益' )
    business_income = models.FloatField(u'营业收入(百万元)' )
    bips = models.FloatField(u'每股主营业务收入(元)' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.esp)

# 营运能力
class OperationData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    arturnover = models.FloatField(u'应收账款周转率(次)' )
    arturndays = models.FloatField(u'应收账款周转天数(天)' )
    inventory_turnover = models.FloatField(u'存货周转率(次)' )
    inventory_days = models.FloatField(u'存货周转天数(天)' )
    currentasset_turnover = models.FloatField(u'流动资产周转率(次)' )
    currentasset_days = models.FloatField(u'流动资产周转天数(天)' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.esp)

# 成长能力
class GrowthData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    mbrg = models.FloatField(u'主营业务收入增长率( %)' )
    nprg = models.FloatField(u'净利润增长率( %)' )
    nav = models.FloatField(u'净资产增长率' )
    targ = models.FloatField(u'总资产增长率' )
    epsg = models.FloatField(u'每股收益增长率' )
    seg = models.FloatField(u'股东权益增长率' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.mbrg)

# 偿债能力
class DebtpayingData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    currentratio = models.FloatField(u'流动比率' )
    quickratio = models.FloatField(u'速动比率' )
    cashratio = models.FloatField(u'现金比率' )
    icratio = models.FloatField(u'利息支付倍数' )
    sheqratio = models.FloatField(u'股东权益比率' )
    adratio = models.FloatField(u'股东权益增长率' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.mbrg)

# 现金流量
class DebtpayingData(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'名称', max_length=50)
    cf_sales = models.FloatField(u'经营现金净流量对销售收入比率' )
    rateofreturn = models.FloatField(u'资产的经营现金流量回报率' )
    cf_nm = models.FloatField(u'经营现金净流量与净利润的比率' )
    cf_liabilities = models.FloatField(u'经营现金净流量对负债比率' )
    cashflowratio = models.FloatField(u'现金流量比率' )

    def __unicode__(self):
        return '%s %s %s' % (self.code, self.name, self.mbrg)