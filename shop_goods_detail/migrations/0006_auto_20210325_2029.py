# Generated by Django 2.2.5 on 2021-03-25 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_goods_detail', '0005_goods_color_other_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods_color_other_img',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='商品顏色', to='shop_goods_detail.Goods_color'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='主商品編號', to='shop_goods_detail.Goods_color'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color_img_1',
            field=models.ImageField(null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片1'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color_img_2',
            field=models.ImageField(null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片2'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color_img_3',
            field=models.ImageField(null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片3'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color_img_4',
            field=models.ImageField(null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片4'),
        ),
        migrations.AlterField(
            model_name='goods_color_other_img',
            name='goods_color_img_5',
            field=models.ImageField(null=True, upload_to='static/upload/images/goods_other_color_img', verbose_name='商品圖片5'),
        ),
    ]