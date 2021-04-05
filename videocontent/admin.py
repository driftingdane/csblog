from django.contrib import admin

from .models import UploadVideo


class VideoAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'video', 'created')


admin.site.register(UploadVideo, VideoAdmin)
