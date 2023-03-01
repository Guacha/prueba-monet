from django.db import models


# Create your models here.
# Test model
class Test(models.Model):
    # Primary key is id
    id = models.AutoField(primary_key=True)

    # Test model has name, and description
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    # test has one or many questions, but each question has only one test

    # Test str method: returns test's name
    def __str__(self):
        return f"""{self.name} <{self.id}>"""


# Question model
class Question(models.Model):
    # Primary key is id
    id = models.AutoField(primary_key=True)

    # Question model has text, and answer
    text = models.CharField(max_length=50)

    # Question has one test, the one that contains it
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    # Question has one or many answers, but each answer has only one question

    # Question str method: returns question's text
    def __str__(self):
        return f"""Question {self.id} for test {self.test}: {self.text}"""


# Answer model
class Answer(models.Model):
    # Primary key is id
    id = models.AutoField(primary_key=True)

    # Answer model has text, and is_correct
    text = models.CharField(max_length=50)
    is_correct = models.BooleanField()

    # Answer has one question, the one that contains it
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class TestQuestion(models.Model):
    # TestQuestion model has test, question, and score
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class StudentTest(models.Model):
    # StudentTest model has student, test, and score
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
