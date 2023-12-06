from django.contrib import admin
from .models import CartItem
from .models import Item

admin.site.register(CartItem)
admin.site.register(Item)


