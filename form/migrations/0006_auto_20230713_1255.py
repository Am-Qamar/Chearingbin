# Generated by Django 3.1 on 2023-07-13 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20230713_1253'),
    ]

    operations = [
         migrations.RunSQL(
            "ALTER TABLE form_fields MODIFY COLUMN new_name TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;",
        ),
    ]