# Generated by Django 3.0.7 on 2020-07-23 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataapp', '0005_auto_20200724_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dataapp.Product'),
        ),
    ]
