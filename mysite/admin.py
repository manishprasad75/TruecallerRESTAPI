from django.contrib import admin
from .models import UserSpam, UsersContact


# Register your models here.
class UsersContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'synced_from_uid']


class UserSpamAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'user']


admin.site.register(UserSpam, UserSpamAdmin)
admin.site.register(UsersContact, UsersContactAdmin)
