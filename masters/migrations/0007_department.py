# Generated by Django 2.2.5 on 2019-09-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_employmentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
