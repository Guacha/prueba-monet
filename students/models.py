from django.db import models


# Create your models here.
# Student model
class Student(models.Model):
    # Primary key is id
    id = models.AutoField(primary_key=True)

    # Student has name, last name, username, and password
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    # Student has one or many tests, but each test has only one student
    tests = models.ManyToManyField('tests.Test', through='tests.StudentTest')

    # Student str method: returns student's username
    def __str__(self):
        return f"""Student {self.id}: {self.username}"""
