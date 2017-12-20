# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.db import models
#
# # Create your models here.
#
# # 新闻事件数据
#
# # 即时新闻
# class LatestNews(models.Model):
#     classify = models.CharField(u'新闻类别', max_length=50)
#     title = models.CharField(u'新闻标题', max_length=50)
#     time = models.DateField(u'发布时间')
#     url = models.CharField(u'新闻链接', max_length=50)
#     content = models.CharField(u'新闻内容', max_length=5000)
#     def __unicode__(self):
#         return '%s %s %s' % (self.time, self.classify, self.title)
#
#
# # 信息地雷
# class Notices(models.Model):
#     title = models.CharField(u'信息标题', max_length=50)
#     type = models.CharField(u'信息类型', max_length=50)
#     time = models.DateField(u'公告日期')
#     url = models.CharField(u'信息内容URL', max_length=50)
#     def __unicode__(self):
#         return '%s %s %s' % (self.name, self.type, self.code)
#
#
# # 信息地雷
# class GubaSina(models.Model):
#     title = models.CharField(u'消息标题', max_length=50)
#     content = models.CharField(u'消息内容', max_length=50)
#     ptime = models.DateField(u'发布时间')
#     rcounts = models.FloatField(u'阅读次数')
#     def __unicode__(self):
#         return '%s %s' % (self.ptime, self.title)