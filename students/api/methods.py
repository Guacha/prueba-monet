from django.contrib.auth import authenticate
from django.shortcuts import redirect, render


# Login method
def auth_login(request, user):
    # Check if user is authenticated
    if user is not None:
        # Log in user
        request.session['user'] = user.username
        # Redirect user to home page
        return redirect('mytests')
    else:
        # Redirect user back to login page
        return redirect('login')


def login(request):
    # Check if request is POST
    if request.method == 'POST':
        # Get username and password from request
        username = request.POST.get('user')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        # Check if user is authenticated
        if user is not None:
            # Log in user
            auth_login(request, user)
            # Redirect user to home page
            return redirect('mytests')
        else:
            # Redirect user back to login page
            return redirect('login')
    else:
        # Render login page
        return redirect('login')