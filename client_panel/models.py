from django.contrib.auth.models import User
from django.db import models


class Kayak(models.Model):
    TYPECHOICE = [
        ('Jednosoboy', 'Jednoosobwy'),
        ('Dwuosobowy', 'Dwuosobowy'),
        ('Trzyosobowy', 'Trzyosobowy')
    ]
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    type = models.CharField(max_length=32, choices=TYPECHOICE)
    available = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return 'Model: {}'.format(self.name)


class Route(models.Model):
    name = models.CharField(max_length=32)
    distance = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return 'Trasa {}'.format(self.name)


class Booking(models.Model):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    term = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    kayak = models.ManyToManyField(Kayak, through='BookingKayaks')

    def __str__(self):
        return 'Rezerwacja: {}, Trasa: {}, Termin: {}, {}'.format(self.user,
                                                                  self.route,
                                                                  self.term,
                                                                  self.time)


class BookingKayaks(models.Model):
    booking = models.ForeignKey(Booking, related_name='reservation', on_delete=models.CASCADE)
    kayak = models.ForeignKey(Kayak, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)