# Generated by Django 3.2.9 on 2022-06-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Загальне',
                'verbose_name_plural': 'Загальні',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Ваше ім'я")),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакти',
            },
        ),
        migrations.CreateModel(
            name='RithualServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('picture', models.TextField(verbose_name='Посилання на фото')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Послуга',
                'verbose_name_plural': 'Послуги',
            },
        ),
        migrations.CreateModel(
            name='Ruthual_goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('picture', models.TextField(verbose_name='Посилання на фото')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
