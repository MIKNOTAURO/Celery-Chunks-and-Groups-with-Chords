# Celery-Chunks-and-Groups-with-Chords
An example which executes a Celery task using Celery Groups and Celery chunks and monitors memory usage

You have to install memory-profiler and line-profiler as root user, run following commands

`sudo pip install memory-profiler`

`sudo pip install line-profiler`
Move to project directory and run Celery Worker
`celery -A tasks worker --concurrency=4 --loglevel=info --autoscale=12,3`

Now simply run the `monitor-usage.py`
