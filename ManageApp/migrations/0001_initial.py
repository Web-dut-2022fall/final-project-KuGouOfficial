# Generated by Django 4.1.3 on 2022-12-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB',
            fields=[
                ('key', models.CharField(max_length=1024, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(max_length=1024)),
            ],
        ),
    ]