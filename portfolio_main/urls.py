from importlib.resources import path
from django.urls import path
from portfolio_main import views

urlpatterns = [
    path('', views.home, name='home')
]