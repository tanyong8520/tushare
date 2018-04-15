# # -*- coding: utf-8 -*-
from django.db import models



class JobInfoModel(models.Model):
    id = models.AutoField(u'编号',primary_key=True)
    fileName = models.CharField(u'文件名', max_length=100)
    type = models.IntegerField(u'类型：1系统，2自定义')
    runDate = models.CharField(u'执行周期', max_length=100)
    describe = models.CharField(u'描述', max_length=200)
    delete = models.IntegerField(u'是否删除：1未删除，2已删除')
    date = models.DateField(u'创建日期')

    def __unicode__(self):
        return self.id
        # 将属性和属性值转换成dict 列表生成式

    def toDict(self):
        return dict([(attr, getattr(self, attr)) for attr in
                     [f.name for f in self._meta.fields]])  # type(self._meta.fields).__name__

    # class Meta:
    #     managed = False
    #     db_table = 'quartz_jobinfomodel'
