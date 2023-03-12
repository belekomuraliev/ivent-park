from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

from park_user.models import Author


def compress_image(img, file_format='png', new_width=None, new_height=None ):
    image = Image.open(img)
    width, height = image.size
    if new_width and new_height:
        image = image.resize((new_width, new_height))
    elif new_width:
        new_height = int(new_width / width * height)
        image = image.resize((new_width, new_height))
    elif new_height:
        new_width = int(new_height / height * width)
        image = image.resize((new_width, new_height))
    image_io = BytesIO()
    image.save(image_io, format=file_format, optimize=True)
    new_image = File(image_io, name=f"{img.name.split('.')[0]}.{file_format}")
    return new_image


class Ivent(models.Model):
    ivetn_id = models.IntegerField()
    image = models.ImageField(upload_to="photos", blank=True)
    title =models.TextField()
    data_start = models.DateField()
    location =  models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image, new_width=500)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Creater(models.Model):
    name = models.CharField(max_length=50)
    activity = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True )
    telegram = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    gmail = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='creater')

    def save(self, *args, **kwargs):
        self.image = compress_image(self.image, new_width=500)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name













