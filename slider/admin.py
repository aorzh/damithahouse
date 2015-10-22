from django.contrib import admin
from slider.models import SliderImage


class SliderImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


admin.site.register(SliderImage, SliderImageAdmin)
