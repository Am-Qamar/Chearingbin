# Generated by Django 3.1 on 2023-07-25 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0006_auto_20230713_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='fields',
            name='width',
            field=models.IntegerField(default=12, verbose_name='寬度'),
        ),
    ]
