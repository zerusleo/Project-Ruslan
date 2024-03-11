from django.db import models


# Create your models here.
class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=10)


class Img(models.Model):
    Image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)



