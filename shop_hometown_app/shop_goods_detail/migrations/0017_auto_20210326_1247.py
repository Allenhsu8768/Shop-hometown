# Generated by Django 2.2.5 on 2021-03-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_goods_detail', '0016_auto_20210326_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods_color',
            name='goods_color_img_2',
        ),
        migrations.RemoveField(
            model_name='goods_color',
            name='goods_color_img_3',
        ),
        migrations.RemoveField(
            model_name='goods_color',
            name='goods_color_img_4',
        ),
        migrations.RemoveField(
            model_name='goods_color',
            name='goods_color_img_5',
        ),
    ]
