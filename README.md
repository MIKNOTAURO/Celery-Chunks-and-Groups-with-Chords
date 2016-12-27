# Celery-Chunks-and-Groups-with-Chords
An example which executes a Celery task using Celery Groups and Celery chunks and monitors memory usage

You have to install memory-profiler and line-profiler and redis-server as root user, run following commands

### Install redis on OSX
`brew install redis`
`brew upgrade redis`

### Install Redis on Ubuntu
`sudo apt-get install redis-server`

### Start Redis Server
`sudo service redis-server start`

### Install Line-Profiler and Memory-Profiler

`sudo pip install memory-profiler`

`sudo pip install line-profiler`

Move to project directory and run Celery Worker

`celery -A tasks worker --concurrency=4 --loglevel=info --autoscale=12,3`

Now simply run the `monitor-usage.py`
