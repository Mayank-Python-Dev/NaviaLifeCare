from django.db import models

from bulk_update_or_create import BulkUpdateOrCreateQuerySet
# Create your models here.
from django.utils.translation import gettext as _


class MedicalData(models.Model):
    objects = BulkUpdateOrCreateQuerySet.as_manager()
    sku_id = models.FloatField(_("sku_id"))
    product_id = models.FloatField(_("product_id"))
    sku_name = models.CharField(_("sku_name"), max_length=200)
    price = models.FloatField(_("price"))
    manufacturer_name = models.CharField(
        _("manufacturer_name"), max_length=500)
    salt_name = models.TextField(_("salt_name"))
    drug_form = models.CharField(_("drug_form"), max_length=100)
    Pack_size = models.CharField(_("Pack_size"), max_length=100)
    strength = models.CharField(_("strength"), max_length=100)
    product_banned_flag = models.CharField(
        _("product_banned_flag"), max_length=100)
    unit = models.CharField(_("unit"), max_length=100)
    price_per_unit = models.FloatField(_("price_per_unit"))

    def __str__(self):
        return '{}'.format(self.sku_name)
