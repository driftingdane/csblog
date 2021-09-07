from django.contrib import admin
from typing import Set
# Register your models here.
from django.contrib.auth.models import PermissionsMixin

from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

@admin.register(NewUser)
class UserAdminConfig(UserAdmin):
	search_fields = ('email', 'user_name', 'first_name',)
	list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'is_superuser',)
	ordering = ('-start_date',)
	list_display = ('email', 'user_name', 'first_name', 'is_active', 'is_staff', 'is_superuser',)
	
	fieldsets = (
		(None, {'fields': ('email', 'user_name', 'first_name',)}),
		('Personal', {'fields': ('about',)}),
		('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups',)}),
		
	)
	
	formfield_overrides = {
		NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
		
	}
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}),
	)
	
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		is_superuser = request.user.is_superuser
		disabled_fields = set()  # type: Set[str]
		
		if not is_superuser:
			disabled_fields |= {
				'user_name',
				'is_superuser',
				'user_permissions',
			}
		
		# Prevent non-superusers from editing their own permissions
		if (
			not is_superuser
			and obj is not None
			and obj == request.user
		):
			disabled_fields |= {
				'is_staff',
				'is_superuser',
				'groups',
				'user_permissions',
			}
		
		for f in disabled_fields:
			if f in form.base_fields:
				form.base_fields[f].disabled = True
		
		return form

# admin.site.register(NewUser, UserAdminConfig)
