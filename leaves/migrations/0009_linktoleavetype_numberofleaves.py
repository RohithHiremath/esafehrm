# Generated by Django 2.2.4 on 2019-11-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0008_auto_20191115_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='linktoleavetype',
            name='numberOfLeaves',
            field=models.SmallIntegerField(default=1),
        ),
    ]
