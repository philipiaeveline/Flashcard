from django.contrib import admin
from .models import Author,Category,Location,Picture

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Picture)
