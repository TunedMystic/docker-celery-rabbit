import os

from celery import task


@task
def say_hello():
    from datetime import datetime
    INV_PATH = os.environ.get('INVENTORY_PATH')

    now = datetime.now()

    # Make absolute filename path.
    f_name = '{}.txt'.format(now.strftime('%b-%d-%Y_%I-%M-%S-%p'))
    filename = os.path.join(INV_PATH, f_name)

    with open(filename, 'wt') as f:
        message = 'Hello! Today\'s date is {}'.format(
            now.strftime('%b-%d-%Y_%I-%M-%S-%p')
        )
        f.write(message)

    return 'Wrote file!'
