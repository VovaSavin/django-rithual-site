from django.contrib import admin
from .models import (
	RithualServices, 
	Ruthual_goods, 
	About, 
	Contacts,
	MainPage,
	Headers,
)
# Register your models here.

@admin.register(Headers)
class HeadersAdmin(admin.ModelAdmin):
	list_display = ["name", "date",]

@admin.register(RithualServices)
class RithualServicesAdmin(admin.ModelAdmin):
	list_display = ["name", "date",]


@admin.register(Ruthual_goods)
class RithualGoodsAdmin(admin.ModelAdmin):
	list_display = ["name", "date",]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ["name", "date",]

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
	list_display = ["name", "phone", "date",]

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
	list_display = ["date", "display_on",]