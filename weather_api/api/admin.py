from django.contrib import admin
from .models import ImageUploadModel
from django.utils.html import format_html


class ImageUploadAdminModel(admin.ModelAdmin):
    list_display = ('image_field', 'get_thumbnail')

    def get_thumbnail(self, obj):
        return format_html(f'<img src="{obj.image_field.url}" style="width:50px;"/>')



admin.site.register(ImageUploadModel, ImageUploadAdminModel)
