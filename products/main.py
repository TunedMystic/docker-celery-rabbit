from celery import Celery

celery = Celery('products-worker')
celery.config_from_object('products.celeryconfig')
celery.autodiscover_tasks(['products'])
