from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.http import JsonResponse

def index(request):
    books = Book.objects.all()
   # return render(request, 'books/book_list.html', {'books': books})
    return render(request, 'home.html', {'books': books})

def book_list(request):
    books = Book.objects.all()
   # return render(request, 'books/book_list.html', {'books': books})
    return render(request, 'book_list.html', {'books': books})

def add_book(request):
    if(request.method == 'POST'):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book details added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book details modified successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        messages.warning(request, 'Book details deleted!')
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})

def view_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books/view_book.html', {'book': book})




# Create your views here.
