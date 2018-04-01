# -*- coding: utf-8 -*-
import time

from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")

class schedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.jobstore = DjangoJobStore()
        self.scheduler.add_jobstore(self.jobstore, "default")
        register_events(self.scheduler)
        self.scheduler.start()
        self.scheduler.resume_job()

    def getJobList(self):
        self.scheduler.get_jobs()

    def addJob(self):
        self.scheduler.add_job()

    def deleteJob(self):
        self.scheduler.remove_job()

    def pauseJob(self):
        self.scheduler.pause_job()

    def resumeJob(self):
        self.scheduler.resume_job()



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
