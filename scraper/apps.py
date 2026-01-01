from django.apps import AppConfig


class ScraperConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "scraper"

    def ready(self):
        # Import signals to ensure they are registered
        import scraper.signals  # noqa
