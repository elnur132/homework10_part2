from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_name, name='default_name'),
    path('add-name/', views.add_name, name='add_name')
]
