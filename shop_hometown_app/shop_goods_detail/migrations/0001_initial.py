# Generated by Django 2.2.5 on 2021-03-16 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0016_auto_20210301_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods_color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_title', models.CharField(max_length=60, verbose_name='商品名稱')),
                ('goods_color', models.CharField(max_length=30, verbose_name='商品顏色')),
                ('goods_color_img', models.ImageField(upload_to='static/upload/images/goods_min', verbose_name='商品顏色路徑')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Goods', verbose_name='商品id')),
            ],
            options={
                'verbose_name': '商品顏色表',
                'verbose_name_plural': '商品顏色表',
                'db_table': 'Goods_color',
            },
        ),
    ]
