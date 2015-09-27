from django.contrib import admin
from models import Room, RoomImage
from image_cropping import ImageCroppingMixin

class RoomImageInline(ImageCroppingMixin, admin.TabularInline):
    model = RoomImage
    min_num = 1
    verbose_name = 'Room picture'
    verbose_name_plural = 'Room pictures'
    show_change_link = True



class RoomAdmin(admin.ModelAdmin):
        inlines = [RoomImageInline, ]
        list_display = ("title",)


admin.site.register(Room, RoomAdmin)
