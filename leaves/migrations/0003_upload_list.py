# Generated by Django 2.2.5 on 2019-11-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0002_holidays'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, upload_to='documents/')),
            ],
        ),
    ]
