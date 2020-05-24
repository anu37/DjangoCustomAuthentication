from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
from .views import CreateAccessView, RefreshAccessView

router = routers.DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("auth/", CreateAccessView.as_view()),
    path("refreshtoken/", RefreshAccessView.as_view())
]
