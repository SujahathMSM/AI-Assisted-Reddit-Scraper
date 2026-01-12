from .tasks import trigger_scrape

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import RedditCommunity



@receiver(post_save, sender=RedditCommunity)
def community_track_changed(sender, instance, created, **kwargs):
    """
    Signal handler that runs every time a RedditCommunity is saved.
    """

    # If the object is newly created, do nothing for now
    if created:
        return

    # If tracking is enabled, this is where we would trigger scraping
    if instance.track:
        trigger_scrape.delay(instance.id)

