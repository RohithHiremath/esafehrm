# Generated by Django 2.2.5 on 2019-11-14 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0004_auto_20191114_1257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='area',
            new_name='location',
        ),
    ]
