from django.contrib import admin
from .models import Sales
from user_management.models import Seller, Discord

admin.site.register(Sales)
admin.site.register(Seller)
admin.site.register(Discord)
