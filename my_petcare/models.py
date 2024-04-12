from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.name
        


class BookedService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    pet_name = models.CharField(max_length=100)
    service_date = models.DateField()
    additional_notes = models.TextField(blank=True)

    def __str__(self):
        return self.pet_name