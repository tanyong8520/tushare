# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 宏观经济数据

# 存款利率
class DepositRate(models.Model):
    date = models.DateField(u'变动日期')
    deposit_type = models.CharField(u'存款种类', max_length=50)
    rate = models.FloatField(u'利率（%）')

    def __unicode__(self):
        return '%s' % (self.date)


# 贷款利率
class DepositRate(models.Model):
    date = models.DateField(u'执行日期')
    loan_type = models.CharField(u'存款种类', max_length=50)
    rate = models.FloatField(u'利率（%）')

    def __unicode__(self):
        return '%s' % (self.date)


# 存款准备金率
class DepositRate(models.Model):
    date = models.DateField(u'变动日期')
    before = models.FloatField(u'调整前存款准备金率（%）')
    now = models.FloatField(u'调整后存款准备金率（%）')
    changed = models.FloatField(u'调整幅度（%）')

    def __unicode__(self):
        return '%s' % (self.date)


# 货币供应量
class MoneySupply(models.Model):
    month = models.DateField(u'统计时间')
    m2 = models.FloatField(u'货币和准货币（广义货币M2）(亿元)')
    m2_yoy = models.FloatField(u'货币和准货币（广义货币M2）同比增长(%)')
    m1 = models.FloatField(u'货币(狭义货币M1)(亿元)')
    m1_yoy = models.FloatField(u'货币(狭义货币M1)同比增长(%)')
    m0 = models.FloatField(u'流通中现金(M0)(亿元)')
    m0_yoy = models.FloatField(u'流通中现金(M0)同比增长(%)')
    cd = models.FloatField(u'活期存款(亿元)')
    cd_yoy = models.FloatField(u'活期存款同比增长(%)')
    qm = models.FloatField(u'准货币(亿元)')
    qm_yoy = models.FloatField(u'准货币同比增长(%)')
    ftd = models.FloatField(u'定期存款(亿元)')
    ftd_yoy = models.FloatField(u'定期存款同比增长(%)')
    sd = models.FloatField(u'储蓄存款(亿元)')
    sd_yoy = models.FloatField(u'储蓄存款同比增长(%)')
    rests = models.FloatField(u'其他存款(亿元)')
    rests_yoy = models.FloatField(u'其他存款同比增长(%)')

    def __unicode__(self):
        return '%s' % (self.month)


# 货币供应量(年底余额)
class MoneySupplyBal(models.Model):
    year = models.DateField(u'统计时间')
    m2 = models.FloatField(u'货币和准货币（广义货币M2）(亿元)')
    m1 = models.FloatField(u'货币(狭义货币M1)(亿元)')
    m0 = models.FloatField(u'流通中现金(M0)(亿元)')
    cd = models.FloatField(u'活期存款(亿元)')
    qm = models.FloatField(u'准货币(亿元)')
    ftd = models.FloatField(u'定期存款(亿元)')
    sd = models.FloatField(u'储蓄存款(亿元)')
    rests = models.FloatField(u'其他存款(亿元)')

    def __unicode__(self):
        return '%s' % (self.year)


# 国内生产总值(年度)
class GdpYear(models.Model):
    year = models.DateField(u'统计年度')
    gdp = models.FloatField(u'国内生产总值(亿元)')
    pc_gdp = models.FloatField(u'人均国内生产总值(元)')
    gnp = models.FloatField(u'国民生产总值(亿元)')
    pi = models.FloatField(u'第一产业(亿元)')
    si = models.FloatField(u'第二产业(亿元)')
    industry = models.FloatField(u'工业(亿元)')
    cons_industry = models.FloatField(u'建筑业(亿元)')
    ti = models.FloatField(u'第三产业(亿元)')
    trans_industry = models.FloatField(u'交通运输仓储邮电通信业(亿元)')
    lbdy = models.FloatField(u'批发零售贸易及餐饮业(亿元)')

    def __unicode__(self):
        return '%s' % (self.year)


# 国内生产总值(季度)
class GdpQuarter(models.Model):
    quarter = models.DateField(u'季度')
    gdp = models.FloatField(u'国内生产总值(亿元)')
    gdp_yoy = models.FloatField(u'国内生产总值同比增长(%)')
    pi = models.FloatField(u'第一产业增加值(亿元)')
    pi_yoy = models.FloatField(u'第一产业增加值同比增长(%)')
    si = models.FloatField(u'第二产业增加值(亿元)')
    si_yoy = models.FloatField(u'第二产业增加值同比增长(%)')
    ti = models.FloatField(u'第三产业增加值(亿元)')
    ti_yoy = models.FloatField(u'第三产业增加值同比增长(%)')

    def __unicode__(self):
        return '%s' % (self.quarter)


#三大需求对GDP贡献
class GdpFor(models.Model):
    year = models.DateField(u'统计年度')
    end_for = models.FloatField(u'最终消费支出贡献率(%)')
    for_rate = models.FloatField(u'最终消费支出拉动(百分点)')
    asset_for = models.FloatField(u'资本形成总额贡献率(%)')
    asset_rate = models.FloatField(u'资本形成总额拉动(百分点)')
    goods_for = models.FloatField(u'货物和服务净出口贡献率(%)')
    goods_rate = models.FloatField(u'货物和服务净出口拉动(百分点)')

    def __unicode__(self):
        return '%s' % (self.year)


#三大产业对GDP拉动
class GdpPull(models.Model):
    year = models.DateField(u'统计年度')
    gdp_yoy = models.FloatField(u'国内生产总值同比增长(%)')
    pi = models.FloatField(u'第一产业拉动率(%)')
    si = models.FloatField(u'第二产业拉动率(%)')
    industry = models.FloatField(u'其中工业拉动(%)')
    ti = models.FloatField(u'第三产业拉动率(%)')

    def __unicode__(self):
        return '%s' % (self.year)


#三大产业贡献率
class GdpContrib(models.Model):
    year = models.DateField(u'统计年度')
    gdp_yoy = models.FloatField(u'国内生产总值(%)')
    pi = models.FloatField(u'第一产业献率(%)')
    si = models.FloatField(u'第二产业献率(%)')
    industry = models.FloatField(u'其中工业献率(%)')
    ti = models.FloatField(u'第三产业献率(%)')

    def __unicode__(self):
        return '%s' % (self.year)


#居民消费价格指数
class Cpi(models.Model):
    month = models.DateField(u'统计月份')
    cpi = models.FloatField(u'价格指数')
    def __unicode__(self):
        return '%s' % (self.month)


#居民消费价格指数
class Ppi(models.Model):
    month = models.DateField(u'统计月份')
    ppiip = models.FloatField(u'工业品出厂价格指数')
    ppi = models.FloatField(u'生产资料价格指数')
    qm = models.FloatField(u'采掘工业价格指数')
    rmi = models.FloatField(u'原材料工业价格指数')
    pi = models.FloatField(u'加工工业价格指数')
    cg = models.FloatField(u'生活资料价格指数')
    food = models.FloatField(u'食品类价格指数')
    clothing = models.FloatField(u'衣着类价格指数')
    roeu = models.FloatField(u'一般日用品价格指数')
    dcg = models.FloatField(u'耐用消费品价格指数')
    def __unicode__(self):
        return '%s' % (self.month)