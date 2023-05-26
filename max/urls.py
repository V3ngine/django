from django import views
from django.urls import path

from  . import views
from .views import logout_user



app_name = 'Books'


urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('registration/', views.RegisterUser.as_view(), name='registr'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('library/<slug:slug_category>', views.Library.as_view(), name='category'),

]