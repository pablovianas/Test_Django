from django.urls import path
from rest_framework import routers

from .views import BookList, BookDetail

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookDetail.as_view())
]
