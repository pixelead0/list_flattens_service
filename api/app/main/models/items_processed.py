import logging

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from app.core.models import SaveReversionMixin, TimestampMixin

logger = logging.getLogger(__name__)


class ItemsProcessed(SaveReversionMixin, TimestampMixin):
    """Processed items with that flattens result."""

    items = models.TextField(
        verbose_name=_("Input"),
        help_text=_("List with multiple levels"),
        max_length=100,
        null=False,
    )

    result = models.TextField(
        verbose_name=_("Output"),
        help_text=_("Flatten list output"),
        max_length=100,
        null=False,
    )

    class Meta:
        verbose_name = _("Lista de Items")
        verbose_name_plural = _("Listas de items")
        # ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.result}"



@receiver(pre_save, sender=ItemsProcessed)
def pre_save_generate_flattens_list(sender, instance, **kwargs):
    """
    Generate a flattens list
    """
    from app.main.helpers import ItemsProcessedHelper

    items_processed_helper = ItemsProcessedHelper()
    instance.result = items_processed_helper.flatten(instance.items)
