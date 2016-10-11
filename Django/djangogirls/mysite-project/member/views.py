from django.shortcuts import render
from django.contrib.auth import \
    authenticate as auth_authenticate, \
    login as auth_login
from django.views.decorators.csrf import csrf_exampt

@csrf_exampt
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth_authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        pass
    else:
        pass
