from __future__ import absolute_import

from celery import Celery

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


app = Celery('proj',
             broker='amqp://',
             backend='amqp://',
             include=['ticks.downloader'])
