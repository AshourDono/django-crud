import os
from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Author
from .forms import BookForm, AuthorForm


# Create your views here.


def show_books(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "book_list/index.html", context=context)


def view_book(request, pk):
    book = Book.objects.get(id=pk)
    author = Author.objects.get(id=book.author_id)
    image = book.image.url.split("/")[-1]

    context = {
        "book": book,
        "author": author,
        "image": image
    }
    return render(request, 'book_list/bookDetails.html', context=context)


def view_author(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author_id=author.id)

    context = {
        "author": author,
        "books": books,
    }
    return render(request, 'book_list/author.html', context=context)


def create_author(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect('create_book')
    else:
        form = AuthorForm()

    context = {
        "form": form
    }
    return render(request, "book_list/createAuthor.html", context=context)


def create_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            print(request.POST["name"])
            print(request.POST)
            book = form.save()
            return redirect('books')
    else:
        form = BookForm()

    context = {
        "form": form
    }
    return render(request, "book_list/createBook.html", context=context)


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    context = {
        "form": form
    }
    return render(request, "book_list/createBook.html", context=context)


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk).delete()
    return redirect('books')
