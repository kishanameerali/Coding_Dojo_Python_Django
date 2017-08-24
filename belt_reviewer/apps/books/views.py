from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Author, Book, Review
from django.contrib import messages

def books_index(request):
    recent_reviews = Review.objects.all().order_by('-created_at')[:3]
    books = Book.objects.all()
    return render(request, 'books/books_index.html', {'reviews': recent_reviews, 'all_books': books})

def add(request):
    authors = Author.objects.all()
    return render(request, 'books/books_add.html', {'all_authors': authors})

def book_info(request, id):
    selected_book = Book.objects.get(id=id)
    return render(request, 'books/books_info.html', {'book': selected_book})

def create_new_review(request): #this is for a new book
    Review.objects.create_review(request.POST, request.session['id'])
    return redirect('/books')

def create_review(request, id): #this is for a existing book
    book = Book.objects.get(id=id)
    submitted_review = {
        'title': book.title,
        'author': book.author.id,
        'rating': request.POST['rating'],
        'comment': request.POST['comment'],
        'new_author': ''
    }
    Review.objects.create_review(submitted_review, request.session['id'])
    return redirect('/books')

def delete_review(request, id):
    the_review = Review.objects.get(id=id)
    the_review.delete()
    return redirect('/books')