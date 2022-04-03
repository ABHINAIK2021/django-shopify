from django.db import models



class Item(models.Model):
    item_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)

class PurchasesItem(models.Model):
    item_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    discount_percentage = models.IntegerField()
    discount_amount = models.DecimalField(max_digits=100, decimal_places=2)
    net_amount = models.DecimalField(max_digits=100, decimal_places=2)
    gst_percentage = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=100, decimal_places=2)
    gross_amount = models.DecimalField(max_digits=100, decimal_places=2)
    added_on = models.DateField()

class SalesItem(models.Model):
    item_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    rate = models.DecimalField(max_digits=100, decimal_places=2)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    discount_percentage = models.IntegerField()
    discount_amount = models.DecimalField(max_digits=100, decimal_places=2)
    net_amount = models.DecimalField(max_digits=100, decimal_places=2)
    gst_percentage = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=100, decimal_places=2)
    gross_amount = models.DecimalField(max_digits=100, decimal_places=2)
    added_on = models.DateField()