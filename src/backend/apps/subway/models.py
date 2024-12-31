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
                print(f"Line {instance.name} is experiencing delays")
                logger.info(f"Line {instance.name} is experiencing delays")
            elif instance.status == SubwayStatus.NORMAL:
                if instance.delay_start_time:
                    instance.total_delay_duration += timezone.now() - instance.delay_start_time
                    instance.delay_start_time = None
                print(f"Line {instance.name} is now recovered")
                logger.info(f"Line {instance.name} is now recovered")

    @classmethod
    def update_statuses(cls, line_name=None):
        """Update statuses for all lines or a specific line."""
        from .mta_data_fetcher import get_latest_line_status

        latest_lines = get_latest_line_status()
        if line_name:
            if line_name not in latest_lines:
                return {}
            latest_lines = {line_name: latest_lines[line_name]}

        with transaction.atomic():
            updated_lines = {}
            for name, status in latest_lines.items():
                line, _ = cls.objects.get_or_create(name=name, defaults={"status": status or SubwayStatus.NORMAL})
                if line.status != status:
                    line.status = status or SubwayStatus.NORMAL
                    line.save()
                updated_lines[name] = line

            return updated_lines

    def get_uptime(self):
        total_time = timezone.now() - self.first_seen

        total_seconds = total_time.total_seconds()
        if total_seconds == 0:
            return 1.0

        delay_seconds = self.total_delay_duration.total_seconds()
        if self.status == SubwayStatus.DELAYED and self.delay_start_time:
            delay_seconds += (timezone.now() - self.delay_start_time).total_seconds()

        return 1 - (delay_seconds / total_seconds)

    def to_dict(self):
        return {"line": self.name, "status": self.status}
