# Celery-Chunks-and-Groups-with-Chords
An example which executes a Celery task using Celery Groups and Celery chunks and monitors memory usage

`pip intall Celery`

`pip install Redis`

Running Celery
`celery -A tasks worker --concurrency=4 --loglevel=info --autoscale=12,3`

**To Monitor Memory usage**

`pip install memory-profiler`

`python -m memory_profiler with_chunk.py`

 *OR*

 `python -m memory_profiler with_group.py`
 
 **To Monitor CPU usage**
uncomment `@profile` decorators in with_chunk.py and with_group.py
run following command while staying in the directory

`/usr/local/bin/kernprof -l -v with_chunk.py`

*OR*

`/usr/local/bin/kernprof -l -v with_group.py`
