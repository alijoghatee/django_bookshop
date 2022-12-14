from django.urls import path

from . import views


urlpatterns = [
    path('', views.BookListView.as_view(), name='books_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='books_detail'),
    path('create/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', views.UpdateBookView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.DeleteBookView.as_view(), name='book_delete'),

]
