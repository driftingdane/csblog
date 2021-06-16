# Generated by Django 3.1.7 on 2021-03-21 21:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('feat_img', models.ImageField(help_text='Only jpg/jpeg files are allowed', upload_to='gallery/', validators=[django.core.validators.validate_image_file_extension])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagecontent_uploadimages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': ('image',),
                'verbose_name_plural': 'images',
            },
        ),
    ]