from django.views import generic
from books.models import Book

from django.shortcuts import get_object_or_404


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

    def get_queryset(self):
        if self.kwargs:
            return Book.objects.filter(pub_date=self.kwargs['date'])
        else:
            return Book.objects.order_by('pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs:
            list_books = Book.objects.order_by('pub_date')

            current_book = get_object_or_404(Book, pub_date=self.kwargs['date'])
            current_page = list(list_books).index(current_book)
            count_books = list_books.count()

            if 0 < current_page < count_books - 1:
                context['next_page'] = str(list(list_books)[current_page + 1].pub_date)
                context['previous_page'] = str(list(list_books)[current_page - 1].pub_date)

            elif 0 == current_page:
                context['next_page'] = str(list(list_books)[current_page + 1].pub_date)

            elif count_books - 1 == current_page:
                context['previous_page'] = str(list(list_books)[current_page - 1].pub_date)

        return context
