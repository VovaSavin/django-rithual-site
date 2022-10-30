from django.db import models

# Create your models here.


class RithualServices(models.Model):
	"""
	Table for services
	"""
	name = models.CharField(max_length=100, verbose_name="Назва")
	description = models.TextField(verbose_name="Опис")
	picture = models.TextField(verbose_name="Посилання на фото")
	price_of = models.CharField(verbose_name="Ціна від", max_length=50, blank=True, null=True)
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
	price_of = models.CharField(verbose_name="Ціна від", max_length=50, blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товари"


class About(models.Model):
	"""Simple text for other description info"""
	font_variant = (
		("З", "Звичайний"),
		("К", "Курсив"),
		("Ж", "Жирний"),
		("ЖК", "Жирний курсив"),
		)

	name = models.CharField(max_length=100, verbose_name="Назва")
	description = models.TextField(verbose_name="Текст")
	font = models.CharField(
		max_length=20, 
		choices=font_variant,
		blank=True,
		default="З",
		verbose_name="Шрифт", 
		help_text="курсив, жирний, звичайний, жирний курсив"
		)
	picture = models.TextField(
		verbose_name="Посилання на фото",
		default="https://hafeleshop.com.ua/uploads/shop/products/main/02205340_0.jpg"
		)
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
	our_address = models.TextField(default="", blank=True, null=True, verbose_name="Ваша адреса")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Контакт"
		verbose_name_plural = "Контакти"


class MainPage(models.Model):
	"""Content for main page"""

	font_variant = (
		("З", "Звичайний"),
		("К", "Курсив"),
		("Ж", "Жирний"),
		("ЖК", "Жирний курсив"),
		)
	header_image = models.TextField(
		verbose_name="Список", 
		default="Текст"
		)
	display_on_list = models.BooleanField(default=False, verbose_name="Показати або приховати Список")
	image = models.TextField()
	display_on = models.BooleanField(default=False)
	description_site = models.TextField(verbose_name="Опис", default="Сайт ритуальних послуг")
	font = models.CharField(
		max_length=20, 
		choices=font_variant,
		blank=True,
		default="З",
		verbose_name="Шрифт", 
		help_text="курсив, жирний, звичайний, жирний курсив"
		)
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Головне фото"
		verbose_name_plural ="Головні фото"


class Headers(models.Model):
	"""For header component"""

	name = models.CharField(verbose_name="Назва", max_length=50)
	image = models.TextField(verbose_name="Зображення шапки сайта")
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Зображення шапки сайта"
		verbose_name_plural ="Зображення шапки сайта"


class MailMessage(models.Model):
	"""Mails and messages from users"""
	mails = models.EmailField(verbose_name="Пошта", max_length=255)
	text = models.TextField(verbose_name="Текст")
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Лист"
		verbose_name_plural ="Листи"
