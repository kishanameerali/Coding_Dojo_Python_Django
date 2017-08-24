from __future__ import unicode_literals
from django.db import models
from ..users.models import User


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return 'Author Name: {}'.format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books')

    def __str__(self):
        return 'Title: {}, Author: {}'.format(self.title, self.author)

class ReviewManager(models.Manager):
    def create_review(self, postData, id):
        author = None
        if len(postData['new_author']) <1:
            author = Author.objects.get(id=postData['author'])
        else:
            author = Author.objects.create(name=postData['new_author'])
        book = None
        if not Book.objects.filter(title=postData['title']):
            book = Book.objects.create(
                title = postData['title'],
                author = author
            )
        else:
            book = Book.objects.get(title=postData['title'])
        return self.create(
            rating = postData['rating'],
            comment = postData['comment'],
            user = User.objects.get(id=id),
            book = book
        )

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()

    def __str__(self):
        return 'Book: {}, Rating: {}, User: {}, Comment: {}'.format(self.book, self.rating, self.user, self.comment)
