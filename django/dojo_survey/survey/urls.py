from django.urls import path
from . import views
urlpatterns = [
    path('', views.survey),
    path('process', views.process)
]