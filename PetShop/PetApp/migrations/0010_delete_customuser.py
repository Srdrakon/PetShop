# Generated by Django 5.0.6 on 2024-07-05 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PetApp', '0009_alter_customuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]