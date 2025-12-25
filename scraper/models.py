from django.db import models

# Create your models here.

class RedditCommunity(models.Model):

    """
    Represents a subreddit discovered by the AI discovery phase.
    Example: r/camping, r/RVLiving
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Subreddit name, e.g. r/camping"
    )

    url = models.URLField(
        unique=True,
        help_text="Full URL to the subreddit"
    )

    members = models.PositiveIntegerField(
        help_text="Number of subscribers at discovery time"
    )

    track = models.BooleanField(
        default=False,
        help_text="Whether this community should be actively scraped"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    

class RedditPost(models.Model):
    """
    Represents a Reddit post scraped from a subreddit.
    """

    community = models.ForeignKey(
        RedditCommunity,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    post_id = models.CharField(
        max_length=50,
        unique=True,
        help_text="Reddit's unique post ID"
    )

    title = models.TextField()

    url = models.URLField()

    upvotes = models.IntegerField(
        help_text="Upvote count at time of scrape"
    )

    comments = models.IntegerField(
        help_text="Comment count at time of scrape"
    )

    posted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Original post creation time"
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.post_id} ({self.community.name})"
