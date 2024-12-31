from django.db import models, transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import datetime
import logging

logger = logging.getLogger(__name__)


class SubwayStatus(models.TextChoices):
    NORMAL = "normal", _("Normal")
    DELAYED = "delayed", _("Delayed")


class SubwayLine(models.Model):
    name = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=10, choices=SubwayStatus.choices, default=SubwayStatus.NORMAL)
    last_update = models.DateTimeField(auto_now=True)
    total_delay_duration = models.DurationField(default=datetime.timedelta(0))
    delay_start_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Line {self.name}"

    @receiver(pre_save, sender="subway.SubwayLine")
    def handle_status_change(sender, instance, **kwargs):
        """Handle subway line status changes via signal."""
        if not instance.pk:  # New instance
            return
        old_instance = SubwayLine.objects.get(pk=instance.pk)
        if old_instance.status != instance.status:
            if instance.status == SubwayStatus.DELAYED:
                instance.delay_start_time = timezone.now()
                logger.info(f"Line {instance.name} is experiencing delays")
            elif instance.status == SubwayStatus.NORMAL:
                if instance.delay_start_time:
                    instance.total_delay_duration += timezone.now() - instance.delay_start_time
                    instance.delay_start_time = None
                logger.info(f"Line {instance.name} is now recovered")

    @classmethod
    def update_statuses(cls, line_name=None) -> dict[str, "SubwayLine"]:
        """Update statuses for all lines or a specific line."""
        from .mta_data_fetcher import mta_client

        latest_statuses = mta_client.get_latest_line_status()
        if line_name:
            if line_name not in latest_statuses:
                return {}

        with transaction.atomic():
            lines = cls.objects.filter(name__in=latest_statuses.keys())
            updated_lines = {}
            now = timezone.now()

            for line in lines:
                new_status = latest_statuses[line.name]

                # Update delay duration if currently delayed
                if line.status == SubwayStatus.DELAYED and line.delay_start_time:
                    time_since_update = now - line.last_update
                    line.total_delay_duration += time_since_update

                # Handle status change
                if line.status != new_status:
                    if new_status == SubwayStatus.DELAYED:
                        line.delay_start_time = now
                    elif line.delay_start_time:
                        line.total_delay_duration += now - line.delay_start_time
                        line.delay_start_time = None
                    line.status = new_status

                line.save()
                updated_lines[line.name] = line

            return updated_lines

    def get_uptime(self):
        now = timezone.now()
        total_time = now - self.created_at
        total_seconds = total_time.total_seconds()

        if total_seconds == 0:
            return 1.0

        # If the line is delayed and delay_start_time is set, add the delay time since the last update
        delay_seconds = self.total_delay_duration
        if self.status == SubwayStatus.DELAYED and self.delay_start_time:
            delay_seconds += now - self.last_update
        delay_seconds = delay_seconds.total_seconds()

        return round(1 - (delay_seconds / total_seconds), 3)

    def to_dict(self):
        return {"line": self.name, "status": self.status}
