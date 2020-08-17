from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('add', views.add),
    path('profile', views.profile),
    path('book/<int:id>', views.book),
    path('favorite/<int:book_id>', views.favorite),
    path('unfavorite/<int:book_id>', views.unfavorite),
    path('delete/<int:id>', views.delete),
    path('books/<int:id>/update', views.update)
]