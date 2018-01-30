# -*- coding: utf-8 -*-
import time

from apscheduler.schedulers.background import BackgroundScheduler

from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, "interval", seconds=1,id='testjob')
def test_job():
    time.sleep(4)
    print("I'm a test job!")
    # raise ValueError("Olala!")


register_events(scheduler)

scheduler.start()
print("Scheduler started!")