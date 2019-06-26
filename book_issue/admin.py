import datetime
from django.contrib import admin
from django.utils.html import format_html
from django.core.mail import send_mail, send_mass_mail
from .models import IssueBook
from library.settings import EMAIL_HOST_USER
from .enum import WITHDRAW, LATE


class IssueBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'issue_by', 'suggest_return_date', 'status', 'accept_by', 'return_date']

    def send_mail(self, email=None, name='There', book='No Name', date=datetime.datetime.now()):
        subject = 'Hi {}'.format(name)
        message = 'We inform you that you took a book name "{}" at {}. Your return date have been expired. Please contact with us as soon as possible. Thanks.'.format(book, date)
        from_email = EMAIL_HOST_USER
        mails = send_mail(subject, message, from_email, [email])


    def get_queryset(self, request):
        queryset = super(IssueBookAdmin, self).get_queryset(request)
        self.request = request
        queryset_withdraw = queryset.filter(status=WITHDRAW)
        email_list = []
        today = datetime.datetime.now().date()
        
        for issued_book in queryset_withdraw:
            if today > issued_book.suggest_return_date:
                self.send_mail(issued_book.user.email, issued_book.user.username, issued_book.book.name, issued_book.suggest_return_date)        
        
        queryset_late = queryset_withdraw.filter(suggest_return_date__lte=today).update(status=LATE)

        return queryset

    list_filter = ('status', 'issue_by', 'accept_by')
    search_fields = ('user__name', 'book__name', 'issue_by__name', 'accept_by__name')
admin.site.register(IssueBook, IssueBookAdmin)