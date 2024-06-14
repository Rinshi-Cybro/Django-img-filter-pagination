from django.contrib import admin
from .models import UserActivity, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserActivity)