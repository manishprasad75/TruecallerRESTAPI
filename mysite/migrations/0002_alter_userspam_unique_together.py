# Generated by Django 3.2.3 on 2021-05-22 12:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userspam',
            unique_together={('user', 'phone')},
        ),
    ]