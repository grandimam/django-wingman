import logging
from django.db import models
from django.core.cache import cache
from simple_history.models import HistoricalRecords

logger = logging.getLogger(__name__)


class WingmanCacheManager(models.Manager):
    PREFIX = 'WINGMAN_SETTINGS_{name}'

    def get_settings(self, name):
        cache_key = self.PREFIX.format(name=name)
        prev_value = cache.get(cache_key)
        if not prev_value:
            try:
                instance = self.get(name=name)
                cache.set(cache_key, instance.value, timeout=self.get(name=name).cache_expiry)
            except Exception as e:
                logger.error('Settings %s is not found: %s', name, str(e))

    def delete_settings(self, name):
        cache.delete(self.get_cache_key(name))


class WingmanSettings(models.Model):
    name = models.CharField(
        max_length=255,
        db_index=True,
        unique=True,
    )
    value = models.BooleanField(default=False)
    cache_expiry = models.IntegerField(
        null=True,
        blank=True,
        default=None,
        help_text='Cache expiry timeout in seconds',
    )
    description = models.TextField(blank=True, null=True)
    history = HistoricalRecords()
    objects = WingmanCacheManager()

    def __str__(self):
        return self.name

    @classmethod
    def get_value(cls, setting):
        return cls.objects.get_settings(setting)
