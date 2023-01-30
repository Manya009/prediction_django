from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("house_predict/", views.house_price_predictor, name="house_price_predictor"),
]
