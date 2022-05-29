from django.contrib import admin
from apps.tickets.models import *

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShoppingCart)
