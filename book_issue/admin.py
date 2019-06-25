from django.contrib import admin
from .models import IssueBook

# Register your models here.
class IssueBookAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'issue_by', 'suggest_return_date', 'status', 'accept_by', 'return_date']
    list_filter = ('status', 'issue_by', 'accept_by')
    search_fields = ('user__name', 'book__name', 'issue_by__name', 'accept_by__name')
admin.site.register(IssueBook, IssueBookAdmin)