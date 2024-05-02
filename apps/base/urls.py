from django.urls import path
from apps.base.views import setting

urlpatterns = [
    path("", setting, name="setting")
]
