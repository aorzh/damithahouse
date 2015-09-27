from django.contrib import admin
from models import House

class HouseAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(House, HouseAdmin)

