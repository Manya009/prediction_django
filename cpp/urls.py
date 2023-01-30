from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="hello"),
    path("car_predict/", views.car_price_predictor, name="car_price_predictor"),
]
