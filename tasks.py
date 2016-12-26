from celery_app import app


@app.task
def group_task(i):
    for x in range(0, 10):
        print "in loop %d" % x
    print "loop for %d" % i
    return i


@app.task
def chunk_task(i):
    arr = []
    for _id in i:
        for x in range(0, 10):
            pass
        arr.append(_id)
    return arr


@app.task
def callback(*args):
    print "callback kamal args=%r" % args


@app.task
def chuncker(ch):
    result = ch()
    print "chunker", result
