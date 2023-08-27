from django.db import models

# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    inventory = models.IntegerField()
