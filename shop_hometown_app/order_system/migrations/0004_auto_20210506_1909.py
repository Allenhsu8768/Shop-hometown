# Generated by Django 2.2.5 on 2021-05-06 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_system', '0003_order_info_order_check_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_info',
            name='order_detial',
        ),
        migrations.AddField(
            model_name='order_info_detail',
            name='orders',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order_system.Order_info', verbose_name='訂單編號'),
        ),
    ]
