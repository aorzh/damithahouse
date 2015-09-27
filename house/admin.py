from django.contrib import admin
from models import Room, House

class RoomAdmin(admin.ModelAdmin):
        list_display = ("title",)


class HouseAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Room, RoomAdmin)
admin.site.register(House, HouseAdmin)

