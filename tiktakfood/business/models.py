from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.utils import timezone

from io import BytesIO
from PIL import Image

import socket 

# Create your models here.

class BusinessCategory(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Business(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business')
    category=models.ForeignKey(BusinessCategory,related_name='business',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    description=models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    x = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    y = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    logo = models.ImageField(upload_to='upload/restaurant_logo/', blank=False)
    image=models.ImageField(upload_to='upload/business_image/',blank=True,null=True)
    thumbnail=models.ImageField(upload_to='upload/business_thumbnail/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://localhost:8000/'+self.image.url
        return ''

    def get_thumbnail(self):
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        if self.thumbnail:
            return 'http://localhost:8000/'+self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return 'http://localhost:8000/'+self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self,image,size=(300,200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io=BytesIO()
        img.save(thumb_io,'JPEG',quality=85)
        thumbnail=File(thumb_io,name=image.name)

        return thumbnail