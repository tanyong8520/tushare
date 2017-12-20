# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.db import models
#
# # Create your models here.
#
# #拆放利率
#
# # Shibor拆放利率
# class Shibor(models.Model):
#     date = models.DateField(u'日期')
#     ON = models.FloatField(u'隔夜拆放利率')
#     W1 = models.FloatField(u'1周拆放利率')
#     W2= models.FloatField(u'2周拆放利率')
#     M1 = models.FloatField(u'1个月拆放利率')
#     M2 = models.FloatField(u'2个月拆放利率')
#     M3 = models.FloatField(u'3个月拆放利率')
#     M6 = models.FloatField(u'6个月拆放利率')
#     M9 = models.FloatField(u'9个月拆放利率')
#     Y1 = models.FloatField(u'1年拆放利率')
#
#     def __unicode__(self):
#         return '%s' % (self.date)
#
#
# # 银行报价数据
# class ShiborQuote(models.Model):
#     date = models.DateField(u'日期')
#     bank = models.CharField(u'名称', max_length=50)
#     ON = models.FloatField(u'隔夜拆放利率')
#     ON_B = models.FloatField(u'隔夜拆放买入价')
#     ON_A = models.FloatField(u'隔夜拆放卖出价')
#     W1_B = models.FloatField(u'1周拆放买入')
#     W1_A = models.FloatField(u'1周拆放卖出')
#     M1_B  = models.FloatField(u'2周拆放买入')
#     M1_A= models.FloatField(u'2周拆放卖出')
#     M2_B  = models.FloatField(u'1个月拆放买入')
#     M2_A = models.FloatField(u'1个月拆放卖出')
#     M3_B  = models.FloatField(u'2个月拆放买入')
#     M3_A = models.FloatField(u'3个月拆放卖出')
#     M6_B  = models.FloatField(u'6个月拆放买入')
#     M6_A = models.FloatField(u'6个月拆放卖出')
#     M9_B  = models.FloatField(u'9个月拆放买入')
#     M9_A = models.FloatField(u'9个月拆放卖出')
#     Y1_B  = models.FloatField(u'1年拆放买入')
#     Y1_A = models.FloatField(u'1年拆放卖出')
#
#     def __unicode__(self):
#         return '%s' % (self.date)
#
#
# # 银行报价数据
# class ShiborMa(models.Model):
#     date = models.DateField(u'日期')
#     bank = models.CharField(u'名称', max_length=50)
#     ON = models.FloatField(u'隔夜拆放利率')
#     ON_B = models.FloatField(u'隔夜拆放买入价')
#     ON_A = models.FloatField(u'隔夜拆放卖出价')
#     W1_B = models.FloatField(u'1周拆放买入')
#     W1_A = models.FloatField(u'1周拆放卖出')
#     M1_B = models.FloatField(u'2周拆放买入')
#     M1_A = models.FloatField(u'2周拆放卖出')
#     M2_B = models.FloatField(u'1个月拆放买入')
#     M2_A = models.FloatField(u'1个月拆放卖出')
#     M3_B = models.FloatField(u'2个月拆放买入')
#     M3_A = models.FloatField(u'3个月拆放卖出')
#     M6_B = models.FloatField(u'6个月拆放买入')
#     M6_A = models.FloatField(u'6个月拆放卖出')
#     M9_B = models.FloatField(u'9个月拆放买入')
#     M9_A = models.FloatField(u'9个月拆放卖出')
#     Y1_B = models.FloatField(u'1年拆放买入')
#     Y1_A = models.FloatField(u'1年拆放卖出')
#
#     def __unicode__(self):
#         return '%s' % (self.date)
#
#
# # 银行报价数据
# class LprData(models.Model):
#     date = models.DateField(u'日期')
#     Y1 = models.FloatField(u'1年贷款基础利率')
#
#     def __unicode__(self):
#         return '%s' % (self.date)
#
#
# # LPR均值数据
# class LprMa(models.Model):
#     date = models.DateField(u'日期')
#     Y1_5 = models.FloatField(u'5日均值')
#     Y1_10 = models.FloatField(u'10日均值')
#     Y1_20 = models.FloatField(u'20日均值')
#
#     def __unicode__(self):
#         return '%s' % (self.date)
