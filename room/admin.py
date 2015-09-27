from django.contrib import admin
from models import Room

class RoomAdmin(admin.ModelAdmin):
        list_display = ("title",)


admin.site.register(Room, RoomAdmin)
