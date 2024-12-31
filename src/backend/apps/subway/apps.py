from django.apps import AppConfig
import threading
import time
import logging

from .models import SubwayLine

logger = logging.getLogger(__name__)


class SubwayConfig(AppConfig):
    name = "subway"

    # def ready(self):
    #     from .models import SubwayLine

    #     threading.Thread(target=self._periodic_update).start()

    # def _periodic_update(self):
    #     while True:
    #         try:
    #             print("Updating statuses...")
    #             SubwayLine.update_all_statuses()
    #             print("Done updating statuses...")
    #             time.sleep(5)  # Update every 5 seconds
    #         except Exception as e:
    #             logger.error(f"Error in periodic update: {str(e)}")
