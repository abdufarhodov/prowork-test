# Generated by Django 3.2.4 on 2021-06-16 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0003_auto_20210616_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_id',
            new_name='photo',
        ),
    ]