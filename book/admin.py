from django.contrib import admin
from .models import Book, BookCategory

# Register your models here.
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ('name', )
admin.site.register(BookCategory, BookCategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'author', 'publisher', 'total', 'soft_copy']

    list_filter = ('category', 'author', 'publisher')
    search_fields = ('name', 'category__name', 'author', 'publisher')
admin.site.register(Book, BookAdmin)
