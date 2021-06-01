from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetRoutes, name = "routes"),
]