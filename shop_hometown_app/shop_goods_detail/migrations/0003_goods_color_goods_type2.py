# Generated by Django 2.2.5 on 2021-03-16 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20210301_0902'),
        ('shop_goods_detail', '0002_auto_20210316_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_color',
            name='goods_type2',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType2', verbose_name='商品樣式'),
        ),
    ]