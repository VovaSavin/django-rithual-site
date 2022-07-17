from django.urls import path

from . import views

urlpatterns = [
    path("rith_services/", views.RithualServicesListView.as_view(), name="services"),
    path("rith_services/<int:pk>/", views.DetailServiceAPI.as_view(), name="services"),
    path("rith_goods/", views.RithualGoodsListView.as_view(), name="goods"),
    path("about/", views.AboutListView.as_view(), name="about"),
    path("contacts/", views.ContactsListView.as_view(), name="contacts"),
    path("main_img/", views.MainPageListView.as_view(), name="img_main")
]