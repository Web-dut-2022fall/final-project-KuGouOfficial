# Generated by Django 4.1.3 on 2022-12-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_item_base_bid_item_create_date_item_cur_bid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='winner',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]