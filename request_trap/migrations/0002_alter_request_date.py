# Generated by Django 3.2.4 on 2021-06-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_trap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
