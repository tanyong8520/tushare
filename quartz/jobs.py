# -*- coding: utf-8 -*-
import time


from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from quartz.utilTools.Loader import Loader

from utilAll.DateUtils import *


scheduler = BackgroundScheduler()
jobstore = DjangoJobStore()
scheduler.add_jobstore(jobstore, "default")
register_events(scheduler)
scheduler.start()

class SchedulerService:
    def __init__(self):
        self.scheduler = scheduler
        # self.scheduler.resume_job()

    def getJobList(self):
        self.scheduler.get_jobs()

    def addJob(self,func,dateExp,funcId):
        dateMap = cron2date(dateExp)
        self.scheduler.add_job(func, 'cron', hour=dateMap.get("hour"), minute=dateMap.get("minute"),
                               second=dateMap.get("second"),day=dateMap.get("day"), month=dateMap.get("month"),
                               week=dateMap.get("week"),id=funcId, replace_existing=True)

    def deleteJob(self,funcId):
        self.scheduler.remove_job(funcId)

    def pauseJob(self,funcId):
        self.scheduler.pause_job(funcId)

    def resumeJob(self,funcId):
        self.scheduler.resume_job(funcId)

def computingWork():
    load = Loader()
    module = load.load("B://livelihood//tushare//function//function1.py")
    function = module["test"]
    function()


if __name__ == '__main__':
    pass

# @register_job(scheduler, 'cron', hour='0-23', minute="*", second="*/4",id='testjob2',replace_existing=True)
# def test_job():
#     time.sleep(4)
#     print("I'm a test job222")
#     # raise ValueError("Olala!")
#
# register_events(scheduler)
#
# scheduler.start()
# print("Scheduler started!")
