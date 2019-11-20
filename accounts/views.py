from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):

    '''
    This is a series of nested if statemtents that guide a user through the signup process
    This first checks if it is a post: this means the user has info and wants to sign up
    This next checks if the passwords match:
    Tries to see if username exists, and if it does, brings the user back to the signup page, and display an error
    If the username doesn't exist (executed through the imported User function DoesNotExist)...
    ...it creates one (User.objects.create user) and adds it to the user variable
    Be sure to add tha pssword=request.POST['password'] within the create_user so that it is properly collected
    It then authenticates the user with auth and redirects the user to the homepage

    '''
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confpassword']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Those passwords don\'t match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    '''
    Check that the user has posted (similar to sign-up)
    Authenticate the user with the auth.authenticate function, which requires a username and password
    Keep in mind the username and the password post variables comes from the login sheet, not the signup, so make sure they
    are synced up with the names of the variables
    Check that the user is authentic with if user is not None: this says that you did get a user back
    Use the auth.login function to log in that user
    Redirect the user to the homepage if they are authenticated
    If they are not authenticated, redirect to login with an error message
    '''
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Oops, username or password is incorrect, or please sign up'})
    return render(request, 'accounts/login.html')

def logout(request):
    '''
    Important: logout needs to be a POST request, not a GET request

    '''

    if request.method == 'POST':
        auth.logout(request)
    return render(request, 'accounts/logout.html')
