# Generated by Django 2.2.5 on 2021-05-06 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0009_auto_20210506_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_info_detail',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='order_info_detail',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='order_info_detail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order_info',
        ),
        migrations.DeleteModel(
            name='Order_info_detail',
        ),
    ]
