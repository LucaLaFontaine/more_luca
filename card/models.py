from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class Card(models.Model):
    class Meta:
        abstract=True

    def __str__(self):
        return self.title


class Carousel(Card):
    title = models.CharField(max_length=255, default='Type of Card')
    description = models.TextField(blank=True, null=True)
    image = ResizedImageField(size=[500, 500], quality=75, upload_to='card_images',)
    date_created = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title
