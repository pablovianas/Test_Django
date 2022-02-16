from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Books, Genre, Author
from .forms.BookForm import AddBookForm


# Create your views here.

class BookCreateView(CreateView):
    model = Books
    form_class = AddBookForm
    
    def form_valid(self, form):
        title = form.cleaned_data['title']

        author_name = self.request.POST.get('author')
        Author.objects.create(name=author_name)

        author_id = Author.objects.filter(name=author_name ).values('id')
    
        isbn = form.cleaned_data['isbn']
        summary = form.cleaned_data['summary']

        books = Books.objects.create(title=title, summary=summary, isbn=isbn, author_id=author_id)
      
        for genre in self.request.POST.getlist('genre'):
            gen = Genre.objects.create(name=genre)
            gen.save()
            books.genre.add(gen)
            books.save()
        
        return redirect('books')
      


class BookUpdateView(UpdateView):
    model = Books
    form_class = AddBookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('books')

    

    

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book_delete.html'
    success_url = reverse_lazy('books')

class BookListView(generic.ListView):
    model = Books
    context_object_name = 'book_list'
    queryset = Books.objects.all().order_by('id')
    template_name = 'books.html'
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Books
    template_name = 'book_detailed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['book_detail'] = get_object_or_404(Books, id=self.object.id)
        context['genres'] = Genre.objects.filter(books=self.object.id)
        context['genres_cont'] = Genre.objects.filter(books=self.object.id).count
        print(context['genres'])

        return context
    