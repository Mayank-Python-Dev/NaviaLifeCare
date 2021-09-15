from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(MedicalData)
class MedicalDataAdmin(admin.ModelAdmin):
    list_display = ('sku_id', 'product_id', 'sku_name', 'price', 'manufacturer_name', 'salt_name',
                    'drug_form', 'Pack_size', 'strength', 'product_banned_flag', 'unit', 'price_per_unit')
