# Celery-Chunks-and-Groups-with-Chords
An example which executes a Celery task using Celery Groups and Celery chunks and monitors memory usage

You can change number of tasks, chunk size and loop limit in `constants.py`

# Steps

## 1- Install Redis-Server

### Install redis on OSX
`brew install redis`

`brew upgrade redis`

### Install Redis on Ubuntu
`sudo apt-get install redis-server`

### Start Redis Server
`sudo service redis-server start`

## 2- Create a virtualenv and install requirements.txt

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## 3- Run Celery worker

`celery -A tasks worker --concurrency=4 --loglevel=info --autoscale=12,3`

## 4- Run `monitor_usage.py`

`python monitor_usage.py`
