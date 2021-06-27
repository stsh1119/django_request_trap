# Generated by Django 3.2.4 on 2021-06-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('remote_ip', models.CharField(max_length=20)),
                ('method', models.CharField(max_length=10)),
                ('scheme', models.CharField(max_length=5)),
                ('query_string', models.CharField(max_length=100)),
                ('query_params', models.CharField(max_length=100)),
                ('cookies', models.TextField()),
                ('headers', models.TextField()),
                ('body', models.TextField()),
            ],
        ),
    ]