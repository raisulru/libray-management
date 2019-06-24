from django.db import models
from users.models import User
from book.models import Book


class IssueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='issue_book_for_user', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='issue_book_for_book', null=True, blank=True)
    # issue_by = 

