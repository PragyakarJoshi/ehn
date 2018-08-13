from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    category_name = models.CharField(max_length = 50)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    registration = models.CharField(max_length=300)
    opening_time = models.CharField(max_length=50)
    closing_time = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"id": self.id})
