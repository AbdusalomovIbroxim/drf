from django.contrib import admin
from .models import Post, Category, SubCategory, Country, City

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Country)
admin.site.register(City)
