from celery import Celery

app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')
accept_content = {
    'CELERY_ACCEPT_CONTENT': ['pickle', 'json', 'msgpack', 'yaml']
}
app.conf.update(accept_content)
