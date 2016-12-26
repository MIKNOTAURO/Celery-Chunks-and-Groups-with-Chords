from memory_profiler import profile as mp
from tasks import group_task, callback
from celery import group, chord
from line_profiler import LineProfiler


@mp
# @profile
def run():
    gp = group([group_task.s(x) for x in range(45000)])
    chrd = chord(gp)(callback.s())
    chrd.get()
if __name__ == '__main__':
    run()
