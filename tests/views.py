from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Test


# Create your views here.

# View to get all tests
@login_required
def get_tests(request):
    # Get all tests for the logged in user
    tests = Test.objects.filter(student=request.user.student)

    # Render tests page
    return render(request, 'tests/MyTests.html', {'tests': tests})


# View to get a test
@login_required
def get_test(request, test_id):

    # Get test
    test = Test.objects.get(id=test_id)

    # Check if test is for the logged in user
    if test.student != request.user.student:
        # Redirect user to home page
        return redirect('login')

    # get questions for the test
    questions = test.question_set.all()

    # Render test page
    return render(request, 'tests/Test.html', {'test': test, 'questions': questions})
