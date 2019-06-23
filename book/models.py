from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.DO_NOTHING, related_name='book_for_category', null=True, blank=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    soft_copy = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

