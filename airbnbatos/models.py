from django.db import models
from djmoney.models.fields import MoneyField
# Create your models here.


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document


class CsvExport(models.Model):
    room_id = models.IntegerField()
    host_id = models.IntegerField()
    room_type = models.CharField(blank=False, max_length=30)
    borough = models.CharField(max_length=30, default="")
    neighborhood = models.CharField(blank=False, max_length=100)
    reviews = models.IntegerField()
    overall_satisfaction = models.CharField(blank=True, max_length=50)
    accommodates = models.IntegerField()
    bedrooms = models.CharField(blank=True, max_length=50)
    price = models.CharField(blank=True, max_length=50)
    minstay = models.CharField(blank=True, max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    last_modified = models.CharField(blank=False, max_length=50)


class TestModel(models.Model):
    test = models.CharField(max_length=30)
