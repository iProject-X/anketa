from django.urls import path
from . import views
from survey.views import startapp,  login_view, profile, login, logout



urlpatterns = [
    path('', startapp, name='startapp') ,
  
    path('profile', profile, name='profile'),
    path('logout', logout, name='logout')
    
]
