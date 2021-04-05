from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('cat_title', 'created_at', 'updated_at')


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'status', 'slug', 'author', 'feat_img', 'thumbnail_preview')
	readonly_fields = ('thumbnail_preview',)
	
	def thumbnail_preview(self, obj):
		return obj.thumbnail_preview
	
	thumbnail_preview.short_description = 'Thumbnail'
	thumbnail_preview.allow_tags = True


admin.site.register(models.Post, AuthorAdmin)
admin.site.register(models.Category, CategoryAdmin)
