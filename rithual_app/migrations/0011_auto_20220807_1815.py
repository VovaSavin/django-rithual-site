# Generated by Django 3.2.9 on 2022-08-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rithual_app', '0010_headers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rithualservices',
            name='how_display_description',
        ),
        migrations.AddField(
            model_name='contacts',
            name='our_address',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='display_on_list',
            field=models.BooleanField(default=False, verbose_name='Показати або приховати Список'),
        ),
        migrations.AddField(
            model_name='rithualservices',
            name='price_of',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ціна від'),
        ),
        migrations.AddField(
            model_name='ruthual_goods',
            name='price_of',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ціна від'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='header_image',
            field=models.TextField(default='Текст', verbose_name='Список'),
        ),
    ]
