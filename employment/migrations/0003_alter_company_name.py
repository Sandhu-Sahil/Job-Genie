# Generated by Django 3.2.9 on 2022-06-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment', '0002_alter_employee_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
