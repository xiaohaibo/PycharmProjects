# Generated by Django 2.1.5 on 2019-01-11 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='index',
            field=models.IntegerField(default=100, verbose_name='顺序'),
        ),
    ]
