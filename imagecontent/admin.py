from django.contrib import admin
from django.http import request
from django.utils.html import format_html
from .models import UploadImage



class ImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'copy_url', 'thumbnail_preview')
	readonly_fields = ('thumbnail_preview',)
	
	def thumbnail_preview(self, obj):
		return obj.thumbnail_preview
	thumbnail_preview.short_description = 'Thumbnail'
	thumbnail_preview.allow_tags = True

	def copy_url(self, obj):
		return format_html(
			'<a href="#" class="btn btn-outline-info btn-sm" data-clipboard-action="copy" data-bs-toggle="tooltip" title="Copied!" data-clipboard-text="http://127.0.0.1:8000{url}">Copy</a>'.format(
				url=obj.feat_img.url,
				#host=request.build_absolute_uri(url)
			))

	copy_url.short_description = 'Copy Url'
	

admin.site.register(UploadImage, ImageAdmin)
