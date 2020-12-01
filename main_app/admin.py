from django.contrib import admin

from .models import Meditation, Category, Profile

admin.site.register(Meditation)
admin.site.register(Category)
admin.site.register(Profile)