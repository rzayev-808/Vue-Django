from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name='Qiymet')
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250, verbose_name='Kategoriya')
    article_body = models.TextField(verbose_name='Mezmun')

    def __str__(self):
        return self.name


