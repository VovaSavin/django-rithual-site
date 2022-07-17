# Generated by Django 3.2.9 on 2022-06-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rithual_app', '0002_contacts_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('display_on', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Головне фото',
                'verbose_name_plural': 'Головні фото',
            },
        ),
    ]