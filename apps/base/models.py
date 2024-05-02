from django.db import models
from timezone_field import TimeZoneField



class Boys(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    time = models.DateTimeField(
        verbose_name="Время"
    )
    timezone = TimeZoneField(default='Asia/Bishkek')


    parent = models.ForeignKey(
        'Parent', related_name='boys', on_delete=models.CASCADE,
        verbose_name="Родитель"
    )
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Мальчик"
        

class Girls(models.Model):
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    time = models.DateTimeField(
        verbose_name="Время"
    )
    timezone = TimeZoneField(default='Asia/Bishkek')

    parent = models.ForeignKey(
        'Parent', related_name='girls', on_delete=models.CASCADE,
        verbose_name="Родитель"
    )
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Девочка"


class Parent(models.Model):

    pass
    
    class Meta:
        verbose_name = "Родитель"



