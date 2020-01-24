from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from book import views

urlpatterns = [
    path('book/', views.BookList.as_view()),
    path('book/detail/<int:pk>/', views.BookDetail.as_view()),
    path('editorial/', views.EditorialList.as_view()),
    path('editorial/detail/<int:pk>/', views.EditorialDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)