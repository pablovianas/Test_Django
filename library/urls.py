from django.urls import path
from .views import BookCreateView, BookUpdateView, BookDeleteView, BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('book/add', BookCreateView.as_view(template_name='books_form.html'), name='add_book'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
    path('book/view/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]