from celery import shared_task
from .models import SubwayLine
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def update_subway_statuses():
    """Update all subway line statuses."""
    logger.info("Subway statuses task running...")
    SubwayLine.update_statuses()
