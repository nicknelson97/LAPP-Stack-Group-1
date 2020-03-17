from django.urls import path
from hwapp import views

urlpatterns = [
    path('', views.index, name='index'),
]