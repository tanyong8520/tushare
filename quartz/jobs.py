# -*- coding: utf-8 -*-
import time


from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
from quartz.utilTools.Loader import Loader

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

    def addJob(self):
        self.scheduler.add_job(computingWork, 'cron', hour='0-23', minute="*", second="*/4", id='testtany', replace_existing=True)

    def deleteJob(self):
        self.scheduler.remove_job()

    def pauseJob(self):
        self.scheduler.pause_job()

    def resumeJob(self):
        self.scheduler.resume_job()

def computingWork():
    load = Loader()
    module = load.load("B://livelihood//tushare//function//function1.py")
    function = module["test"]
    function()


if __name__ == '__main__':
    schedulerService = SchedulerService()
    schedulerService.computingWork(1)
    # schedulerService.addJob()

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
