# Generated by Django 2.2.5 on 2019-09-26 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0004_jobgrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salarycomponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentname', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
            ],
        ),
    ]
