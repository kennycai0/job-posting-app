from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    path('signup', views.MySignupView.as_view(), name='signup'),
    path('login', views.MyLoginView.as_view(), name='login')
]
