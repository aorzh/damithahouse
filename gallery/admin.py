from django.contrib import admin
from models import GalleryImage, Gallery, Category
from image_cropping import ImageCroppingMixin


class GalleryImageInline(ImageCroppingMixin, admin.TabularInline):
    model = GalleryImage
    min_num = 1
    verbose_name = 'Image'
    verbose_name_plural = 'Images'
    show_change_link = True
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, ]
    list_display = ("title", "category_name",)
    list_filter = ['title', "category_name"]
    list_display_links = ['title', "category_name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
