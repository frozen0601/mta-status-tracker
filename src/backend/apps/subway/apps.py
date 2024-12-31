from django.apps import AppConfig
import threading
import time
import logging

logger = logging.getLogger(__name__)


class SubwayConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "subway"

    def ready(self):
        from .models import SubwayLine

        # Define all MTA subway lines
        from .mta_data_fetcher import mta_client

        subway_lines = mta_client.get_subway_line_names()
        for line in subway_lines:
            SubwayLine.objects.get_or_create(name=line)
