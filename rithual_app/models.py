from django.db import models

# Create your models here.


class RithualServices(models.Model):
	"""
	Table for services
	"""
	name = models.CharField(max_length=100, verbose_name="Назва")
	description = models.TextField(verbose_name="Опис")
	picture = models.TextField(verbose_name="Посилання на фото")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Послуга"
		verbose_name_plural ="Послуги"

class Ruthual_goods(models.Model):
	"""Table for rithual goods"""
	name = models.CharField(max_length=100, verbose_name="Назва")
	description = models.TextField(verbose_name="Опис")
	picture = models.TextField(verbose_name="Посилання на фото")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товари"

class About(models.Model):
	"""Simple text for other description info"""
	name = models.CharField(max_length=100, verbose_name="Назва")
	description = models.TextField(verbose_name="Текст")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Загальне"
		verbose_name_plural = "Загальні"

class Contacts(models.Model):
	"""Контакти"""
	name = models.CharField(max_length=100, verbose_name="Ваше ім'я")
	phone = models.CharField(max_length=100, verbose_name="Телефон")
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Контакт"
		verbose_name_plural ="Контакти"

class MainPage(models.Model):
	"""Content for main page"""
	image = models.TextField()
	display_on = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Головне фото"
		verbose_name_plural ="Головні фото"

