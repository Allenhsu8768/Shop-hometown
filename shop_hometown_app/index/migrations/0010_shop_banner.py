# Generated by Django 2.2.5 on 2021-02-24 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_remove_goodstype2_goodstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='橫幅名稱')),
                ('Banner_Url', models.ImageField(upload_to='images/Banners')),
                ('GoodsType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType', verbose_name='主類別')),
            ],
            options={
                'verbose_name': '橫幅表',
                'verbose_name_plural': '橫幅表',
                'db_table': 'Shop_Banner',
            },
        ),
    ]
