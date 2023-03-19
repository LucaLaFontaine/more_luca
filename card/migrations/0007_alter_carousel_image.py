# Generated by Django 4.0.10 on 2023-03-14 02:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_remove_carousel_attachment_carousel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, scale=None, size=[500, 500], upload_to='card_images'),
        ),
    ]