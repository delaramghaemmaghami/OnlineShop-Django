import os.path
import re

from django.core.exceptions import ValidationError
from django.db import models
from colorfield.fields import ColorField


class Store(models.Model):
    def validate_phone(self):
        pattern = re.compile("09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}")
        if not pattern.match(str(self.phone)):
            raise ValidationError(f"{self.phone} is not a valid phone number!")

    name = models.CharField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=15, validators=[validate_phone])
    location = models.CharField(max_length=200)
    about_store = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    def get_upload_path(self, filename):
        ext = filename.split(".")[-1]
        filename = f"{self.name}.{ext}"
        path = f"images/goods/"
        return os.path.join(path, filename)

    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to=get_upload_path, blank=False)
    price = models.IntegerField()
    color = ColorField(default="black")
    factory_date = models.DateField()
    store_name = models.ManyToManyField(Store)

    def __str__(self):
        return self.name
