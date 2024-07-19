from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=226, verbose_name='Город')
    count = models.IntegerField(verbose_name='Количество запросов', default=0)

    def __str__(self):
        return self.name, self.count

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
