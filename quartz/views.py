# -*- coding: utf-8 -*-


from django.http import HttpResponse

import json

from quartz.jobs import SchedulerService,computingWork
from quartz.models import JobInfoModel
from utilAll.FileUtils import *
from utilAll.DateUtils import *
from utilAll.ResponseUtils import MakeResponse


def index(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        print req
        return HttpResponse(u"add new work")
    if request.method == 'GET':
        print 'get info'
        return HttpResponse(u"hellow work")
        # JobInfoModel()
    # SchedulerService().addJob(computingWork, '0/10 * * * * * *', 'test1')


def list(request):
    jobInfoList = JobInfoModel.objects.all();
    return MakeResponse(jobInfoList)

def add(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        # fileName = str(request.FILES['file'])
        # handle_upload_file(request.FILES['file'], fileName)
        fileName = 'test'
        type=2
        if(req.has_key("runDate") is False):
            return HttpResponse(status=400)
        else:
            runDate = req.get('runDate')
        if (req.has_key("describe")):
            describe = req.get('describe')
        delete = 1
        date = getNowDate()
        JobInfoModel(fileName=fileName,runDate=runDate,type=type,describe=describe,delete=delete,date=date).save()
        return HttpResponse('success')
    else:
        return HttpResponse(status=403,reason=u'info error')

def initWork(request):
    jobInfoList = JobInfoModel.objects.all();

    return HttpResponse(u"hellow work")