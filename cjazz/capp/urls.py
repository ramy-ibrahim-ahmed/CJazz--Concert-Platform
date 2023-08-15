from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('ticket/', views.ticket, name='ticket'),
]