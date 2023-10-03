from django.db import models

# Create your models here.

class Color_Shades(models.Model):
    color_shades =  models.CharField(max_length=100)

    def __str__(self):
        return self.color_shades


class Color(models.Model):
    color_name = models.CharField(max_length=100)
    shades = models.OneToOneField(Color_Shades , on_delete=models.CASCADE, null=True , blank = True )

    def __str__(self):
        return self.color_name



class Person(models.Model):
    
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    color = models.ForeignKey(Color,on_delete=models.CASCADE ,null=True,blank=True, related_name="color")

    def __str__(self):
        return self.name