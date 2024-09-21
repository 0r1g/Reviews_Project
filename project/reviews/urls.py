from django.urls import path
from . import views

urlpatterns = [
    path('reviews', views.show_reviews, name='show_reviews'),
]
