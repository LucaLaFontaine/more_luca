from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class ImageSet(models.Model):
    def default(self):
        return self.photos



class Card(models.Model):
    class Meta:
        abstract=True

    def __str__(self):
        return self.title

class Carousel(Card):
    title = models.CharField(max_length=255, default='Type of Card')
    description = models.TextField(blank=True, null=True)
    # imageSet = models.OneToOneField(ImageSet, related_name='model', on_delete=models.CASCADE, primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.title

class Photo(models.Model):
    imageSet = models.ForeignKey(Carousel, related_name="photos", on_delete=models.CASCADE)
    image = ResizedImageField(size=[500, 500], quality=75, upload_to='card_images', blank=True, null=True)
    alt = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.description




