from django.db import models



class JobInfo(models.Model):
    id = models.AutoField(u'编号')
    fileName = models.CharField(u'文件名', max_length=100)
    type = models.IntegerField(u'类型：1系统，2自定义')
    runDate = models.CharField(u'执行周期', max_length=100)
    describe = models.CharField(u'描述', max_length=200)
    delete = models.IntegerField(u'是否删除：1未删除，2已删除')
    date = models.DateField(u'创建日期')
