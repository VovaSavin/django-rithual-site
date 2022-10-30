from django.core.mail import send_mail
# from rest_framework.permissions import IsAdminUser
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    ListRithualServicesSerializer,
    ListRithualGoodsSerializer,
    ListAboutSerializer,
    ListContactsSerializer,
    MainPageSerializer,
    HeadersServicesSerializer,
    MailMessageSerializer,
)
from .models import (
    RithualServices,
    Ruthual_goods,
    About,
    Contacts,
    MainPage,
    Headers,
    MailMessage,
)


# Create your views here.

class HeadersListView(ListAPIView):
    """For display headers info"""

    queryset = Headers.objects.all()
    serializer_class = HeadersServicesSerializer


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


class ShowMail(ListCreateAPIView):
    """Display and send mails"""

    def post(self, request, *args, **kwargs):
        mails = MailMessageSerializer(data=request.data)
        if mails.is_valid():
            mails.save()
        send_mail(
            request.data["mails"],
            request.data["text"],
            request.data["mails"],
            ["volodimirsavin56@gmail.com", ],
        )
        return Response(status=201)

    def get_queryset(self):
        return MailMessage.objects.all()

    serializer_class = MailMessageSerializer
