# Generated by Django 2.2.5 on 2021-02-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20210224_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='Images_url',
            field=models.ImageField(upload_to='static/upload/images/goods_min', verbose_name='圖片路徑'),
        ),
        migrations.AlterField(
            model_name='shop_banner',
            name='Banner_Url',
            field=models.ImageField(upload_to='static/upload/images/Banners'),
        ),
    ]
