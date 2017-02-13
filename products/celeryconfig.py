BROKER_URL = 'amqp://guest:guest@rabbit:5672'
CELERY_RESULT_BACKEND = 'rpc'


# Celery config.
CELERYBEAT_SCHEDULE = {
    'every-second': {
        'task': 'products.tasks.say_hello',
        'schedule': 5.0,
    },
}
