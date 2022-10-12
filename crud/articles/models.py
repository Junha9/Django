from django.db import models
from django.conf import settings
from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField
# Create your models here.

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source = 'image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality' : 80},
    )

    def __str__(self):
        return self.title