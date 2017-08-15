Assignment: Dojo Ninjas
Create a new app called 'dojo_ninjas'.

Dojo
Have it include the name of the dojo and the city and state of each dojo
Have the first dojo be "CodingDojo Silicon Valley" in "Mountain View", "CA".
Have the second dojo be "CodingDojo Seattle" in "Seattle", "WA".
Have the third dojo be "CodingDojo New York" in "New York", "NY".

Student
Have it include first_name, last_name of each student in the dojo.
Each dojo can have multiple students and each student belongs to a specific dojo.
This is what you'll do:

Start a new app (the name of the app should be 'dojo_ninjas')
Create appropriate tables/models that allows you to perform tasks such as
Dojo.objects.first().ninjas
Ninja.objects.first().dojo

Using Django Shell:

Create 3 dojos

Dojo.objects.create(name='CodingDojo Silicon Valley', city='Mountain View', state='CA')
Dojo.objects.create(name='CodingDojo Seattle', city='Seattle', state='WA')
Dojo.objects.create(name='CodingDojo New York', city='New York', state='NY')

Delete the three dojos you created (e.g. Dojo.objects.get(id=1).delete())

Dojo.objects.get(id=1).delete()
Dojo.objects.get(id=2).delete()
Dojo.objects.get(id=3).delete()

Create 3 additional dojos by using Dojo.objects.create

Dojo.objects.create(name='CodingDojo Washington', city='Washington DC', state='MD')
Dojo.objects.create(name='CodingDojo Dallas', city='Dallas', state='TX')
Dojo.objects.create(name='CodingDojo Chicago', city='Chicago', state='IL')

Create 3 students that belong to the first dojo you created.

Student.objects.create(first_name='Bradley', last_name='Beal', dojo=Dojo.objects.get(id=4))
Student.objects.create(first_name='John', last_name='Wall', dojo=Dojo.objects.get(id=4))
Student.objects.create(first_name='Otto', last_name='Porter', dojo=Dojo.objects.get(id=4))


Create 3 more students and have them belong to the second dojo you created.

Student.objects.create(first_name='Harrison', last_name='Barnes', dojo=Dojo.objects.get(id=5))
Student.objects.create(first_name='Dirk', last_name='Nowitzki', dojo=Dojo.objects.get(id=5))
Student.objects.create(first_name='Yogi', last_name='Ferrell', dojo=Dojo.objects.get(id=5))

Create 3 more students and have them belong to the third dojo you created.

Student.objects.create(first_name='Zach', last_name='LaVine', dojo=Dojo.objects.get(id=6))
Student.objects.create(first_name='Dwayne', last_name='Wade', dojo=Dojo.objects.get(id=6))
Student.objects.create(first_name='Kris', last_name='Dunn', dojo=Dojo.objects.get(id=6))

Be able to retrieve all students that belong to the first Dojo

Dojo.objects.get(id=4).student_set.all()
Or
Student.objects.filter(dojo=4)

Be able to retrieve all students that belong to the last Dojo

Dojo.objects.get(id=6).student_set.all()
Or
Student.objects.filter(dojo=6)

Add a new field in the Dojo class (found in your models.py) called 'desc'. Allow 'desc' to hold long text (more than 255 characters). To forward engineer the change, run the appropriate migration commands. Successfully run the migration files and check the records to make sure the new field was added successfully.

Dojo.objects.get(id=4)
<Dojo: Name: CodingDojo Washington, City: Washington DC, State: MD, Desc: <class 'django.db.models.fields.TextField'>>
