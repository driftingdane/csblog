from django.core.validators import validate_email, validate_unicode_slug, MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


class Contact(models.Model):
	name = models.CharField(max_length=200, validators=[MaxValueValidator(50), MinValueValidator(3)])
	email = models.CharField(max_length=100, validators=[validate_email])
	message = models.TextField(blank=True, validators=[validate_unicode_slug])
	contact_date = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__(self):
		return self.name
