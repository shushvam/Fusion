# Generated by Django 3.0.6 on 2020-06-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central_mess', '0008_auto_20200522_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthly_bill',
            name='month',
            field=models.CharField(default=6, max_length=20),
        ),
    ]
