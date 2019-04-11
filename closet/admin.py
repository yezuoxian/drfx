from django.contrib import admin

from .models import UserProfile, Product, Collocation

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Collocation)
