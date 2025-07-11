from django.urls import path
from spotify.views import home,login_view,logout_view
urlpatterns = [
   path('',home,name="home"),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
]