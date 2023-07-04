from django.contrib import admin
from . models import books, members, borrowbooks, returnbook


admin.site.register(books)
admin.site.register(members)
admin.site.register(borrowbooks)
admin.site.register(returnbook)

# Register your models here.
