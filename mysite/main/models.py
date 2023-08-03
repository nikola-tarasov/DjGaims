from django.db import models

# Create your models here.


class Gaim(models.Model):
    img = models.ImageField(upload_to='image/%Y')
    name_gaim = models.CharField(max_length=100)
    description_gaims = models.TextField(max_length=2000)
    

    def __str__(self):
        return self.name_gaim
    
class Comments(models.Model):
    name = models.CharField(max_length= 50, null=True )
    text = models.TextField(max_length= 2000 , null=True)
    post = models.ForeignKey(Gaim, related_name='comments', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name

class Likes(models.Model):
    ip = models.CharField(max_length=100, null=True)
    pos = models.ForeignKey(Gaim, related_name='commentslike', on_delete=models.CASCADE)


    def __str__(self):
        return self.ip
    