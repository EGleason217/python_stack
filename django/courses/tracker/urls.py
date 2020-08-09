from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('<int:id>/destroy', views.destroy),
    path('<int:id>/comment', views.create_comment),
    path('<int:id>', views.comments),
]
