from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import FileExtensionValidator


class Video(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
	                           related_name='videocontent_uploadvideos')
	created = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=100)
	video = models.FileField(upload_to='videos/',
	                         validators=[FileExtensionValidator(allowed_extensions=('mp4',))],
	                         help_text=('Only mp4 files are allowed'),
	                         )
	
	class Meta:
		verbose_name = 'video',
		verbose_name_plural = 'videos'
	
	def __str__(self):
		return self.title

