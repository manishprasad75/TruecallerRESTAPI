from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'phone', 'is_spam']


admin.site.register(UserProfile, UserProfileAdmin)
