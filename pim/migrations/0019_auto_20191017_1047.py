# Generated by Django 2.2.4 on 2019-10-17 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0018_auto_20191017_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_details',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.Department'),
        ),
    ]
