from memory_profiler import profile as mp
from line_profiler import LineProfiler
from tasks import group_task, callback
from celery import chord


@mp
# @profile
def run():
    chunk = group_task.chunks(zip(range(100)), 10)
    chrd = chord(chunk.group())(callback.s())
    chrd.get()
if __name__ == '__main__':
    run()
