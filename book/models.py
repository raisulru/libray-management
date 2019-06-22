from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
