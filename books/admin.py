from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
# Register your models here.

admin.site.register(Book, BookAdmin)
from django.contrib import admin

# Register your models here.
