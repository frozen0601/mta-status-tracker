from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
import datetime
import logging

logger = logging.getLogger(__name__)


class SubwayLine(models.Model):
    name = models.CharField(max_length=10, unique=True)
    is_delayed = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now=True)
    total_delay_duration = models.DurationField(default=datetime.timedelta(0))
    delay_start_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Line {self.name}"


@receiver(pre_save, sender=SubwayLine)
def log_status_change(sender, instance, **kwargs):
    try:
        old_instance = SubwayLine.objects.get(pk=instance.pk)
        if old_instance.is_delayed != instance.is_delayed:
            if instance.is_delayed:
                logger.info(f"Line {instance.name} is experiencing delays")
                instance.delay_start_time = timezone.now()
            else:
                logger.info(f"Line {instance.name} is now recovered")
                if instance.delay_start_time:
                    delay_duration = timezone.now() - instance.delay_start_time
                    instance.total_delay_duration += delay_duration
                    instance.delay_start_time = None
    except SubwayLine.DoesNotExist:
        pass
