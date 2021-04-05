from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import validate_image_file_extension
from PIL import Image
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


class UploadImage(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='imagecontent_uploadimages')
	title = models.CharField(max_length=150)
	created = models.DateTimeField(default=timezone.now)
	feat_img = models.ImageField(upload_to="gallery/",
	                             validators=[validate_image_file_extension],
	                             help_text=('Only jpg/jpeg files are allowed'),
	                             )
	
	## Resize and save the image
	def save(self, *args, **kwargs):
		super(UploadImage, self).save(*args, **kwargs)
		imag = Image.open(self.feat_img.path)
		if imag.width > 800 or imag.height > 600:
			size_big = (800, 600)
			imag.thumbnail(size_big)
			imag.save(self.feat_img.path)
	
	@property
	def thumbnail_preview(self):
		if self.feat_img:
			_thumbnail = get_thumbnail(self.feat_img,
			                           '200x150',
			                           upscale=False,
			                           crop=False,
			                           quality=100)
			return format_html(
				'<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
		return ""
	
	class Meta:
		verbose_name = 'image',
		verbose_name_plural = 'images'
	
	def __str__(self):
		return self.title