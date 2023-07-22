from django.db import models

# Create your models here.


class Gaim(models.Model):
    img = models.ImageField(upload_to='image/%Y', null=True)
    name_gaim = models.CharField(max_length=100)
    description_gaims = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.name_gaim
