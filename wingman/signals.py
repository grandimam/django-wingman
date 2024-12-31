from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from wingman.models import WingmanSettings
from django.dispatch import receiver


@receiver(post_save, sender=WingmanSettings)
@receiver(post_delete, sender=WingmanSettings)
def invalidate_cache(sender, instance, **kwargs):
    WingmanSettings.objects.delete(instance.name)
