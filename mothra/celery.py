from __future__ import absolute_import

import os

import sys
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mothra.settings')

app = Celery('mothra')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# app.conf.update(
#     CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
# )

if hasattr(settings, "LATINO_BIN_PATH"):
    import clr
    sys.path.append(settings.LATINO_BIN_PATH)
    import LatinoInterfaces



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def test_task():
    print "test!"
    return 1


@app.task()
def sum_task(a,b):
    return a+b


