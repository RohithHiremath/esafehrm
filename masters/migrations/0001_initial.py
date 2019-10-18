# Generated by Django 2.2.5 on 2019-10-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Employmentstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employementstatus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=50)),
                ('jobdescription', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Jobcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobcategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jobgrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobgrade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salarycomponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentname', models.CharField(max_length=50)),
                ('types', models.CharField(max_length=50)),
            ],
        ),
    ]
