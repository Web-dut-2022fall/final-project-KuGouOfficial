# Generated by Django 4.1.3 on 2022-12-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageApp', '0002_remove_db_key_db_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db',
            name='id',
        ),
        migrations.AddField(
            model_name='db',
            name='key',
            field=models.CharField(default=0, max_length=1024, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]