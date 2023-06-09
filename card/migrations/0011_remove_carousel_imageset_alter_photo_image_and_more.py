# Generated by Django 4.0.10 on 2023-03-19 03:47

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_imageset_remove_carousel_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='imageSet',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=75, scale=None, size=[500, 500], upload_to='more_luca/media/card_images'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='imageSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='card.carousel'),
        ),
    ]
