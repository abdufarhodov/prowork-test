# Generated by Django 3.2.4 on 2021-06-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0002_rename_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='cat_id',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='proapp.photo'),
            preserve_default=False,
        ),
    ]
