# Generated by Django 2.2.5 on 2019-11-04 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0003_auto_20191104_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linktoleavetype',
            name='leave_structure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.Leavestructure'),
        ),
    ]
