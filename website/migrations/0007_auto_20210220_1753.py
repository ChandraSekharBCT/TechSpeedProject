# Generated by Django 2.2.5 on 2021-02-20 12:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_signup'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='signups',
        ),
    ]
