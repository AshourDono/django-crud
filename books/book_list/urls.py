from django.urls import path
from .views import edit_book, view_book, show_books, view_author, create_book, delete_book, create_author

urlpatterns = [
    path('', show_books, name='books'),
    path('<int:pk>/', view_book, name='book'),
    path('author/<int:pk>/', view_author, name='author'),
    path('createbook/', create_book, name='create_book'),
    path('createauthor/', create_author, name='create_author'),
    path('editbook/<int:pk>/', edit_book, name='edit_book'),
    path('deletebook/<int:pk>/', delete_book, name='delete_book')
]
