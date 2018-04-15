from django.http import HttpResponse
from quartz.jobs import SchedulerService,computingWork
from quartz.models import JobInfoModel
import json

def index(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        print 'post info'
        print req
        return HttpResponse(u"add new work")
    if request.method == 'GET':
        print 'get info'
        return HttpResponse(u"hellow work")
        # JobInfoModel()
    # SchedulerService().addJob(computingWork, '0/10 * * * * * *', 'test1')


def initWork(request):
    jobInfoList = JobInfoModel.objects.all();

    return HttpResponse(u"hellow work")