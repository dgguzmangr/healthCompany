# Generated by Django 4.2.2 on 2023-07-10 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='discharge_data',
            new_name='discharge_date',
        ),
    ]
