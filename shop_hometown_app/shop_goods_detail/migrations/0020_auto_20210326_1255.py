# Generated by Django 2.2.5 on 2021-03-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_goods_detail', '0019_goods_color_goods_color_img_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods_color',
            name='goods_color_img_1',
        ),
        migrations.AddField(
            model_name='goods_color',
            name='goods_color_img_2',
            field=models.ImageField(blank=True, null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片2'),
        ),
    ]
