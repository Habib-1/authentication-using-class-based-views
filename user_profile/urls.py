from django.urls import path
from . views import home,create_account,Log_in,profile,edit_profile,change_pass
from .import views

urlpatterns = [
    path('',home.as_view(),name='home'),
    path('register/',create_account.as_view(),name="register"),
    path('login/',Log_in.as_view(),name='login'),
    path('profile/',profile.as_view(),name='profile'),
    path('logout/',views.logout,name='logout'),
    path('update_profile/<int:pk>/',edit_profile.as_view(),name='edit_profile'),
    path('password_change/',change_pass.as_view(),name='change_pass'),
   
]