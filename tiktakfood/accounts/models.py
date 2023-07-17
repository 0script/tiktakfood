from django.contrib.auth.models import AbstractUser
from django.db import models

import datetime

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.EmailField( unique=True)
    address=models.CharField(max_length=255)
    sex=models.CharField(max_length=1,default='M')
    age=models.DateField(default=datetime(1999,12,9))
    # will use django group 
    # is_delivery=models.BooleanField(_("is a delivery agent"),default=False)
    # is_admin=models.BooleanField(_("is administrator for restaurant"),default=False)
    # is_owner=models.BooleanField(_("is owner of restaurant page"),default=False)
    # pass
    # # add additional fields in here

    def __str__(self):
        return self.username
    