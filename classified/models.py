# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# 参考数据

# 行业分类
class Industry(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    c_name = models.CharField(u'行业名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)

# 概念分类
class Concept(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    c_name = models.CharField(u'行业名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)

# 地域分类
class Area(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    c_name = models.CharField(u'行业名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 中小板分类
class Sme(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 风险警示板分类
class St(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)



# 沪深300成份及权重
class St(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    date = models.DateField(u'日期')
    weight = models.FloatField(u'权重')
    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 上证50成份股
class Sz50s(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 上证50成份股
class Zz500s(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 终止上市股票列表
class Terminated(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    oDate = models.DateField(u'上市日期')
    tDate = models.DateField(u'终止上市日期')

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)


# 暂停上市股票列表
class Suspended(models.Model):
    code = models.CharField(u'代码', max_length=50)
    name = models.CharField(u'股票名称', max_length=50)
    oDate = models.DateField(u'上市日期')
    tDate = models.DateField(u'终止上市日期')

    def __unicode__(self):
        return '%s %s %s' % (self.name, self.code)