from django.urls import path
from .views import nippoListView #ポイント1

urlpatterns = [
    path("", nippoListView, name="nippo-list")
]