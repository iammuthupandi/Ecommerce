from django.contrib import admin
from .models import *

# class CategoryAdmine(admin.ModelAdmin):
#     list_display = ('name','image','description')

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Favourite)
