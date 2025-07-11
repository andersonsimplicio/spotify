from django.urls import path
from spotify.views import home
urlpatterns = [
   path('',home,name="home")
]