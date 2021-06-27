from django.urls import path
from .views import VacancyCreateView
from . import views

urlpatterns = [
    path('', views.home, name='vacancy-home'),
    path('new', VacancyCreateView.as_view(), name='vacancy-new')
]
