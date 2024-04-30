from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Record(models.Model):
    sum = models.FloatField()
    text = models.TextField()
    date = models.DateField()
    includes_items = models.BooleanField(default=False)
    is_income = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, through='RecordCategory', null=True)

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse('record_update', args=[str(self.id)])


class Item(models.Model):
    name = models.TextField()
    cost = models.FloatField()
    category = models.ManyToManyField(Category, through='ItemCategory')
    record = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True)
    amount = models.FloatField(null=True)

    def __str__(self):
        return self.name


class RecordCategory(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class ItemCategory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
