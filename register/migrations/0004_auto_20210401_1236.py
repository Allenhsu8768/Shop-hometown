# Generated by Django 2.2.5 on 2021-04-01 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20210401_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_member',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.City', verbose_name='城市'),
        ),
        migrations.AddField(
            model_name='user_member',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.Country', verbose_name='國家'),
        ),
        migrations.AlterField(
            model_name='user_member',
            name='is_Active',
            field=models.BooleanField(default=False, verbose_name='帳號是否驗證成功'),
        ),
    ]