from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator, MinValueValidator


class Customer(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    name = models.CharField(max_length=20)
    address = models.TextField()
    mailid = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message="Phone: 10 digits allowed.")

    contact = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    lastservice = models.DateField()
    investment = models.FloatField(default=0)
    age = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(60), MinValueValidator(18)], error_messages={'validators': 'Age greater than 60 and less than 18 is not allowed'})
    gender = models.CharField(
        max_length=9, choices=GENDER_CHOICES, default='1')

    def __str__(self):
        return self.name
