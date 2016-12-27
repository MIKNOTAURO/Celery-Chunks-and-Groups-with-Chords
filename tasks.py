"""
This module contains Celery tasks
"""
from celery_app import app
from constants import LOOP_RANGE


@app.task
def group_task(_id):
    for x in range(LOOP_RANGE):
        print "in loop %d" % x
    print "loop for %d" % _id
    return _id


@app.task
def callback(*args):
    print "callback kamal args=%r" % args
