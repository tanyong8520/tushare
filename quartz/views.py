from django.http import HttpResponse
from quartz.jobs import SchedulerService,computingWork


def index(request):
    SchedulerService().addJob(computingWork, '0/10 * * * * * *', 'test1')
    return HttpResponse(u"hellow work")

def initWork(request):
    return HttpResponse(u"hellow work")