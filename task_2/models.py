from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Product(models.Model):
    article = models.CharField(verbose_name='Article', max_length=10)
    brand = models.CharField(verbose_name='Brand', max_length=30)
    title = models.CharField(verbose_name='Title', max_length=50)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
