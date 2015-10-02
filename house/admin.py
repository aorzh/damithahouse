from django.contrib import admin
from models import House, HouseImage
from image_cropping import ImageCroppingMixin


class HouseImageInline(ImageCroppingMixin, admin.TabularInline):
    model = HouseImage
    min_num = 1
    verbose_name = 'House picture'
    verbose_name_plural = 'House pictures'
    show_change_link = True
    extra = 0


class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline, ]
    list_display = ("title",)
    list_filter = ['title', "rooms"]

admin.site.register(House, HouseAdmin)

