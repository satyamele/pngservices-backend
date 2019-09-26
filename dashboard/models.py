from django.db import models


class Customer(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=20)
    address = models.TextField()
    mailid = models.EmailField()
    contact = models.PositiveIntegerField()
    lastservice = models.DateField()
    investment = models.FloatField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(
        max_length=9, choices=GENDER_CHOICES, default='1')

    def __str__(self):
        return self.name
