<<<<<<< HEAD
from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contacts/', views.contacts_view, name='contacts'),
=======
# catalog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
>>>>>>> d9679e90beb07769dcace178c687f635124c8a43
]
