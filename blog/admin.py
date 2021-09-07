from django.contrib import admin
from blog.models import Post
from . import models


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('cat_title', 'created_at', 'updated_at')


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category', 'status', 'slug', 'thumbnail_preview')
	readonly_fields = ('thumbnail_preview',)
	prepopulated_fields = {'slug': ('title',)}
	
	# Restrict staff users to only change their own posts
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser or request.user.groups.filter(name='admins').exists():
			return qs
		return qs.filter(author=request.user)
	
	# def has_change_permission(self, request, obj=None):
	# 	if request.user.groups.filter(name='admins').exists():
	# 		return True
	# 	return False
	
	# def has_change_permission(self, request, obj=None):
	# 	return False
	#
	# def has_add_permission(self, request, obj=None):
	# 	return True
	#
	# def has_delete_permission(self, request, obj=None):
	# 	return False
	#
	# def has_view_permission(self, request, obj=None):
	# 	return True
	
	def thumbnail_preview(self, obj):
		return obj.thumbnail_preview
	
	thumbnail_preview.short_description = 'Thumbnail'
	thumbnail_preview.allow_tags = True
	
	class Meta:
		model = Post
		exclude = ('slug',)


admin.site.register(models.Post, AuthorAdmin)
admin.site.register(models.Category, CategoryAdmin)

# Register all models with for loop #
# import django.apps
#
# models = django.apps.apps.get_models()
# print(models)
#
# for model in models:
# 	try:
# 		admin.site.register(model)
# 	except admin.sites.AlreadyRegistered:
# 		pass

# unregister models from admin areas
# admin.site.unregister(django.contrib.sessions.models.Session)
