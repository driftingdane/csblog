from django.contrib import admin
from .models import UploadVideo
from django.utils.html import format_html

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'copy_url', 'created')
	
	def copy_url(self, obj):
		return format_html(
			'<a href="#" class="btn btn-outline-info btn-sm" data-clipboard-action="copy" data-bs-toggle="tooltip" title="Copied!" data-clipboard-text="http://127.0.0.1:8000{url}">Copy</a>'.format(
				url=obj.video.url,
				#host=request.build_absolute_uri(url)
			))

	copy_url.short_description = 'Copy Url'


admin.site.register(UploadVideo, VideoAdmin)
