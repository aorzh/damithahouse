from django.contrib import admin
from models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(Video, VideoAdmin)