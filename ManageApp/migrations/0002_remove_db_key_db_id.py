# Generated by Django 4.1.3 on 2022-12-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db',
            name='key',
        ),
        migrations.AddField(
            model_name='db',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
