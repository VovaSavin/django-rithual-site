from rest_framework import serializers
from .models import (
	RithualServices, 
	Ruthual_goods, 
	About, 
	Contacts,
	MainPage,
)

class ListRithualServicesSerializer(serializers.ModelSerializer):
	"""Serializer for services"""

	class Meta:
		model = RithualServices
		fields = "__all__"
		

class ListRithualGoodsSerializer(serializers.ModelSerializer):
	"""Serializer for services"""

	class Meta:
		model = Ruthual_goods
		fields = "__all__"



class ListAboutSerializer(serializers.ModelSerializer):
	"""Serializer for services"""

	class Meta:
		model = About
		fields = "__all__"


class ListContactsSerializer(serializers.ModelSerializer):
	"""Serializer for services"""

	class Meta:
		model = Contacts
		fields = "__all__"


class MainPageSerializer(serializers.ModelSerializer):
	"""Serializer for MainPage"""

	class Meta:
		model = MainPage
		fields = "__all__"
