# Generated by Django 3.2.9 on 2022-07-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rithual_app', '0004_auto_20220719_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='font',
            field=models.CharField(blank=True, choices=[('З', 'Звичайний'), ('К', 'Курсив'), ('Ж', 'Жирний'), ('ЖК', 'Жирний курсив')], default='З', help_text='курсив, жирний, звичайний, жирний курсив', max_length=20, verbose_name='Шрифт'),
        ),
    ]
