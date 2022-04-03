from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.models import Item, PurchasesItem, SalesItem
import datetime

def index(request):
    purchasesItem = PurchasesItem.objects.count()
    salesItem = SalesItem.objects.count()
    return render(request, 'home.html', {'purchasesItem': purchasesItem, 'salesItem': salesItem})

def sales(request):
    items = Item.objects.raw('SELECT id, item_name, qty FROM myapp_item WHERE qty <> 0')

    if request.method == 'POST':
        salesItem = SalesItem(
            item_name=request.POST.get('salesItemName'), 
            qty=request.POST.get('salesQty'), 
            rate=request.POST.get('salesRate'), 
            amount = request.POST.get('salesAmount'),
            discount_percentage = request.POST.get('salesDiscountPercentage'),
            discount_amount = request.POST.get('salesDiscountAmount'),
            net_amount = request.POST.get('salesNetAmount'),
            gst_percentage = request.POST.get('salesGSTPercentage'),
            gst_amount = request.POST.get('salesGSTAmount'),
            gross_amount = request.POST.get('salesGrossAmount'),
            added_on = datetime.datetime.now()
            )
        salesItem.save()

        i = Item.objects.get(item_name=request.POST.get('salesItemName'))
        i.qty = i.qty - int(request.POST.get('salesQty'))
        i.save()

        return redirect('inventory')
    return render(request, 'sales.html', {'items': items})

def purchases(request):
    if request.method == 'POST':
        purchasesItem = PurchasesItem(
            item_name=request.POST.get('purchasesItemName'), 
            qty=request.POST.get('purchasesQty'), 
            rate=request.POST.get('purchasesRate'), 
            amount = request.POST.get('purchasesAmount'),
            discount_percentage = request.POST.get('purchasesDiscountPercentage'),
            discount_amount = request.POST.get('purchasesDiscountAmount'),
            net_amount = request.POST.get('purchasesNetAmount'),
            gst_percentage = request.POST.get('purchasesGSTPercentage'),
            gst_amount = request.POST.get('purchasesGSTAmount'),
            gross_amount = request.POST.get('purchasesGrossAmount'),
            added_on = datetime.datetime.now()
            )
        purchasesItem.save()
        
        check = Item.objects.filter(item_name=request.POST.get('purchasesItemName')).exists()
        if not check:
            i = Item(
                item_name=request.POST.get('purchasesItemName'), 
                qty=request.POST.get('purchasesQty'), 
                rate=request.POST.get('purchasesRate')
                )
            i.save()
        else:
            j = Item.objects.get(item_name=request.POST.get('purchasesItemName'))
            j.qty = j.qty + int(request.POST.get('purchasesQty'))
            j.rate = request.POST.get('purchasesRate')
            j.save()

        return redirect('inventory')
    return render(request, 'purchases.html')

def inventory(request):
    items = Item.objects.raw('SELECT id, item_name, qty, rate, (qty*rate) AS amount FROM myapp_item WHERE qty <> 0')
    return render(request, 'inventory.html', {'items': items})