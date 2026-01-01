from django.contrib import admin
from .models import RedditCommunity, RedditPost


@admin.register(RedditCommunity)
class RedditCommunityAdmin(admin.ModelAdmin):
    list_display = ("name", "members", "track", "created_at")
    list_filter = ("track",)
    search_fields = ("name",)
    ordering = ("-members",)


@admin.register(RedditPost)
class RedditPostAdmin(admin.ModelAdmin):
    list_display = ("post_id", "community", "upvotes", "comments", "updated_at")
    list_filter = ("community",)
    search_fields = ("post_id", "title")
    ordering = ("-updated_at",)
