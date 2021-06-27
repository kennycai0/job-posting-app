from django.urls import path
from . import views
from .views import ResumeCreateView


urlpatterns = [
    path('', views.home, name='resume-home'),
    path('new', ResumeCreateView.as_view(), name='resume-new')
]
