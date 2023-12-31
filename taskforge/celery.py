from celery import Celery
import os

#---------------------------------------------------------- CELERY_SETTINGS ---------------------------------------------------------
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbl_backend.settings.base')
app = Celery('tbl_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')