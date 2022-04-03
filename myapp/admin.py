from django.contrib import admin
from myapp.models import Item, PurchasesItem, SalesItem


admin.site.register(Item)
admin.site.register(PurchasesItem)
admin.site.register(SalesItem)