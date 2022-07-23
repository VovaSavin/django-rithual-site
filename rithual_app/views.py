from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from .serializers import (
	ListRithualServicesSerializer,
	ListRithualGoodsSerializer,
	ListAboutSerializer,
	ListContactsSerializer,
	MainPageSerializer,
)
from .models import (
	RithualServices, 
	Ruthual_goods, 
	About, 
	Contacts,
	MainPage
)
# Create your views here.

class RithualServicesListView(ListAPIView):
	"""For display rithual services"""
	queryset = RithualServices.objects.all()
	serializer_class = ListRithualServicesSerializer

class RithualGoodsListView(ListAPIView):
	"""For display rithual goods"""
	queryset = Ruthual_goods.objects.all()
	serializer_class = ListRithualGoodsSerializer

class AboutListView(ListAPIView):
	"""For display about page"""
	queryset = About.objects.all().order_by("id")
	serializer_class = ListAboutSerializer

class ContactsListView(ListAPIView):
	"""For display contacts"""
	queryset = Contacts.objects.all()
	serializer_class = ListContactsSerializer


class DetailServiceAPI(RetrieveAPIView):
	"""For one service"""

	queryset = RithualServices.objects.all()
	serializer_class = ListRithualServicesSerializer

class DetailGoodsAPI(RetrieveAPIView):
	"""For one service"""

	queryset = Ruthual_goods.objects.all()
	serializer_class = ListRithualGoodsSerializer


class MainPageListView(ListAPIView):
	"""For display contacts"""
	queryset = MainPage.objects.all()
	serializer_class = MainPageSerializer
