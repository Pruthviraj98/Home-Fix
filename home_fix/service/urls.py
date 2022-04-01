from django.urls import path
from . import views

app_name = "service"
urlpatterns = [
    path("request_service/", views.request_service_view, name="request_service"),
    path("offer_service/", views.offer_service_view, name="offer_service"),
]
