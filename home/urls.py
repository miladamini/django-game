from . import views
from django.urls import path

appname = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='homeView')
]
