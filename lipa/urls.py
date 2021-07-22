from django.urls import path
from . import views

urlpatterns = [
    # Ck Mall Homepage
    path('', views.index, name='index'),
]
