from django.contrib import admin

from .models import UploadImage


class ImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'feat_img', 'created', 'thumbnail_preview')
	
	readonly_fields = ('thumbnail_preview',)

	def thumbnail_preview(self, obj):
		return obj.thumbnail_preview

	thumbnail_preview.short_description = 'Thumbnail'
	thumbnail_preview.allow_tags = True


admin.site.register(UploadImage, ImageAdmin)
