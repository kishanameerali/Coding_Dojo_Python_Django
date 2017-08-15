Assignment: Books/Authors
Create a new app called 'book_authors' in the same project where you did the previous assignment: Dojo Ninjas.  You'll use this assignment as well as the previous assignment to learn about Ajax.
Please do the following
	1.	Create a new model called 'Book' with the information above.
	2.	Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the following:
	1.	Book.objects.first().authors
	2.	Author.objects.first().books
	3.	Successfully create and run the migration files
	4.	Using the shell...

Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby

Book.objects.create(name="C sharp", desc="C# by Microsoft")
Book.objects.create(name="Java, desc="Not about coffee")
Book.objects.create(name="Python", desc="Not about the snake")
Book.objects.create(name="PHP", desc="Lamp Stuff")
Book.objects.create(name="Ruby", desc="Ride the Rails")

Create 5 different authors: Mike, Speros, John, Jadee, Jay

Author.objects.create(first_name="Mike", last_name="Choi", email="mchoi@dojo.com")
Author.objects.create(first_name="Speros", last_name="Misirlakis", email="sperosm@dojo.com")
Author.objects.create(first_name="John", last_name="Smith", email="johnsmith@dojo.com")
Author.objects.create(first_name="Jadee", last_name="Drew", email="jadee@dojo.com")
Author.objects.create(first_name="Jay", last_name="Buhner", email="jbuhner@dojo.com")

Add a new field in the authors table called 'notes'.  Make this a TextField.  Successfully create and run the migration files.

Change the name of the 5th book to C#

w = Book.objects.get(id=5)
w.name = "C#"
w.save()

Change the first_name of the 5th author to Ketul

a = Author.objects.get(id=5)
a.first_name = "Ketul"
a.save()

Assign the first author to the first 2 books

Author.objects.get(id=1).books.add(Book.objects.get(id=1))
Author.objects.get(id=1).books.add(Book.objects.get(id=2))

Assign the second author to the first 3 books

Author.objects.get(id=2).books.add(Book.objects.get(id=1))
Author.objects.get(id=2).books.add(Book.objects.get(id=2))
Author.objects.get(id=2).books.add(Book.objects.get(id=3))

Assign the third author to the first 4 books

Author.objects.get(id=3).books.add(Book.objects.get(id=1))
Author.objects.get(id=3).books.add(Book.objects.get(id=2))
Author.objects.get(id=3).books.add(Book.objects.get(id=3))
Author.objects.get(id=3).books.add(Book.objects.get(id=4))

Assign the fourth author to the first 5 books (or in other words, all the books)

Author.objects.get(id=4).books.add(Book.objects.get(id=1))
Author.objects.get(id=4).books.add(Book.objects.get(id=2))
Author.objects.get(id=4).books.add(Book.objects.get(id=3))
Author.objects.get(id=4).books.add(Book.objects.get(id=4))
Author.objects.get(id=4).books.add(Book.objects.get(id=5))

For the 3rd book, retrieve all the authors

Book.objects.get(id=3).author_set.all()

For the 3rd book, remove the first author

Author.objects.get(id=2).books.remove(Book.objects.get(id=3))

For the 2nd book, add the 5th author as one of the authors

Author.objects.get(id=5).books.add(Book.objects.get(id=2))

Find all the books that the 3rd author is part of

Author.objects.get(id=3).books.all()

Find all the books that the 2nd author is part of

Author.objects.get(id=2).books.all()