# Generated by Django 2.2.5 on 2021-03-16 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20210301_0902'),
        ('shop_goods_detail', '0003_goods_color_goods_type2'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_color',
            name='goods_type',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType', verbose_name='商品主類別'),
        ),
    ]
