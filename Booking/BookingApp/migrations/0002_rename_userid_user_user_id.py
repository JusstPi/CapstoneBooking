# Generated by Django 4.2.1 on 2023-05-20 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookingApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userID',
            new_name='user_id',
        ),
    ]