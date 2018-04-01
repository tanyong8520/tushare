from django.http import HttpResponse
from quartz.jobs import SchedulerService

def index(request):
    SchedulerService().addJob()
    return HttpResponse(u"hellow work")