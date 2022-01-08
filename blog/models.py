from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from tinymce.models import HTMLField
from django.core.validators import validate_image_file_extension
from PIL import Image
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
	cat_title = models.CharField(max_length=150, verbose_name="title")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="created at")
	
	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"
		ordering = ['cat_title']
	
	def __str__(self):
		return self.cat_title


class Post(models.Model):
	class NewManager(models.Manager):
		
		def get_queryset(self):
			return super().get_queryset().filter(status='published')
	
	options = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	
	title = models.CharField(max_length=250)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
	excerpt = models.TextField(blank=True, null=True)
	feat_img = models.ImageField(upload_to="post_img/",
	                             validators=[validate_image_file_extension],
	                             help_text=('Only jpg/jpeg files are allowed'),
	                             blank=True, null=True)
	content = HTMLField()
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	publish = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
	status = models.CharField(max_length=10, choices=options, default='draft')
	objects = models.Manager()  # default manager
	newmanager = NewManager()  # custom manager
	
	def get_absolute_url(self):
		return reverse('blog:post_single', args=[self.slug])
	
	## Resize and save the image
	def save(self, *args, **kwargs):
		super(Post, self).save(*args, **kwargs)
		if self.feat_img:
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
		# return ""
		
		else:
			pass
	
	class Meta:
		ordering = ('publish',)
	
	def __str__(self):
		return self.title
