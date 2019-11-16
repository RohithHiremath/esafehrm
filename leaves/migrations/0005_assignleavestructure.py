# Generated by Django 2.2.4 on 2019-11-08 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pim', '0001_initial'),
        ('leaves', '0004_auto_20191104_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignLeaveStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('updatedDate', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('empid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pim.Personal_details')),
                ('leave_structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaves.Leavestructure')),
            ],
        ),
    ]
