import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def trigger_scrape(community_id):
    """
    Dummy Celery task.
    Later this will trigger Bright Data scraping.
    """
    logger.info(
        f"[CELERY TASK] Scrape triggered for community_id={community_id}"
    )
