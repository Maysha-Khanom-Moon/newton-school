from django.db import models

# Create your models here.


# student Schema
class Student(models.Model):
    '''
    django automatically add this field --> it's a counter
    id = models.AutoField()
    
    It's a primary key: which never repeat
    '''
    
    name = models.CharField(max_length=100)  # more than 100 char will show error
    age = models.IntegerField(default=18)  # kono value pass na korle default value 18 hobe
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    # image = models.ImageField()
    # file = models.FileField()


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name
    