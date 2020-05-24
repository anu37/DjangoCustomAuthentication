from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import UrlShorterView

router = routers.DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("urlshort/", UrlShorterView.as_view()),
]
