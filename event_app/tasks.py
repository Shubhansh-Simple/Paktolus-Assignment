# event_app/tasks.py

# python
import logging

# 3rd party
from celery import shared_task


# Using the logger defined in django's settings LOGGING
logging.getLogger('celery.worker.strategy').setLevel(logging.WARNING)
logging.getLogger('celery.worker').setLevel(logging.WARNING)
logging.getLogger('kombu').setLevel(logging.WARNING)
#logging.getLogger('celery').setLevel(logging.INFO)                      # or ERROR/CRITICAL
logger = logging.getLogger('celery')


@shared_task
def log_to_file(event_id):
    '''Logging to a file through celery task'''

    # Logging the new event creationg into "celery.log" file
    logger.info(f'"New event received: [{event_id}]"')
