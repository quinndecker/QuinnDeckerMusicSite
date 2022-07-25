from django.urls import reverse
from operator import truediv
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, unique=True, null='true')
    show_date = models.CharField(max_length=200, unique=False, null='true')
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    address = models.CharField(max_length=200, unique=True, null='true')
    content = RichTextField(blank='true', null='true')
    created_on = models.DateTimeField(auto_now_add=True)
    meta_description = models.CharField(max_length=160, unique=True, null='true')
    cover_image = models.ImageField(null='true',blank='true', upload_to='thumbnails/')
    thumb = ImageSpecField(source = 'cover_image', processors=[ResizeToFit(300,462)], format='PNG')
    cover_image_alt = models.CharField(max_length=200, default = 'STRING')
    #image = models.ImageField(null='true',blank='true', upload_to='images/')
    #smart = ImageSpecField(source = 'image', processors = [SmartResize(500,300)], format='PNG')
    #image_alt = models.CharField(max_length=200, default = 'STRING')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.slug)])