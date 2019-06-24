from django.db import models
from users.models import User
from book.models import Book
from .enum import ISSUE_STATUS, WITHDRAW


class IssueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='issue_book_for_user', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='issue_book_for_book', null=True, blank=True)
    issue_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='issue_book_for_issue_by', null=True, blank=True)
    accept_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='issue_book_for_accept_by', null=True, blank=True)
    issue_date = models.DateField(auto_now_add=True)
    suggest_return_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=ISSUE_STATUS, default=WITHDRAW)
