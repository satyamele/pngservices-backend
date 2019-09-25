from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    mailid = models.EmailField()
    contact = models.PositiveIntegerField()
    lastservice = models.DateField()
    price = models.FloatField(default=100)

    def __str__(self):
        return self.name
