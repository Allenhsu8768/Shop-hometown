# Generated by Django 2.2.5 on 2021-04-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20210411_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_member',
            name='user_age',
            field=models.IntegerField(null=True, verbose_name='年齡'),
        ),
        migrations.AlterField(
            model_name='user_member',
            name='check_emaill_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='信箱驗證成功時間'),
        ),
    ]
