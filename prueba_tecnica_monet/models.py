from django.db import models


# Student model
class Student(models.Model):
    # Student model has name, last name, email, and password
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    # Each student has one or many tests
    tests = models.ManyToManyField('Test', through='StudentTest')


# Test model
class Test(models.Model):
    # Test model has name, and description
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    # test has one or many questions
    questions = models.ManyToManyField('Question', through='TestQuestion')


# Question model
class Question(models.Model):
    # Question model has text, and answer
    text = models.CharField(max_length=50)

    # Question has one test, the one that contains it
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


# Answer model
class Answer(models.Model):
    # Answer model has text, and is_correct
    text = models.CharField(max_length=50)
    is_correct = models.BooleanField()

    # Answer has one student, the one who answered
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # Answer has one question, the one that was answered
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


# StudentTest model
class StudentTest(models.Model):
    # StudentTest model has student, test, and score
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()


class TestQuestion(models.Model):
    # TestQuestion model has test, question, and score
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class QuestionAnswer(models.Model):
    # QuestionAnswer model has question, answer, and score
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
