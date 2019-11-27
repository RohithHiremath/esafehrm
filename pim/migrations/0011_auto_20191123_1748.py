# Generated by Django 2.2.4 on 2019-11-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0010_auto_20191122_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_details',
            old_name='emailid',
            new_name='companyemailid',
        ),
        migrations.AddField(
            model_name='personal_details',
            name='personalemailid',
            field=models.EmailField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
