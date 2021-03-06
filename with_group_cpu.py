"""
This module runs a celery task Synchronously(Just to monitor memory/CPU usage,
although we can run it Asynchronously). This module builds a group of celery task for each parameter.
It enqueues each task in Message Queue(Tsk Queue) for each parameter. PS: It builds 45000 tasks.
"""
# App Specific imports
from constants import TOTAL_TASKS
from tasks import group_task, callback
# 3rd Party Imports
from celery import group, chord


@profile  # Decorator for line_profiler (CPU Usage)
def run():
    """
    This module runs group of Celery tasks for 45000 parameters
    """
    # Creating a group of tasks for 45000 parameters
    gp = group([group_task.s(x) for x in range(TOTAL_TASKS)])
    # Creating a Celery Chord for the group of tasks to receive callback when group finishes
    celery_chord = chord(gp)(callback.s())
    # Running tasks
    celery_chord.get()
if __name__ == '__main__':
    run()
