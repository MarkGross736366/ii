from django.contrib import admin
from index.models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ["author", "title"]
    search_fields = ["author", "title"]

class Meta:
    model = Book

admin.site.register(Book, BookAdmin)
admin.site.register(Message)