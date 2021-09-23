from django.contrib import admin
from django.contrib.sites.models import Site

from .models import Video
from django.utils.html import format_html


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'copy_url', 'created')
	
	def copy_url(self, obj):
		h = Site.objects.get_current().domain
		# full_url = ''.join(['http://', get_current_site(request).domain, obj.get_absolute_url()])
		return format_html(
			'<a href="#" class="btn btn-outline-info btn-sm" data-clipboard-action="copy" data-bs-toggle="tooltip" title="Copied!" data-clipboard-text="{site}/{url}">Copy</a>'.format(
				url=obj.video,
				site=h,
			))
	
	copy_url.short_description = 'Copy Url'
