from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # пост запрос через форму, аудит
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # аутентификация, достаём данные из БД чтобы понять есть ли такой пользователь
            if user:
                auth.login(request, user)        # авторизация
                return HttpResponseRedirect('/')  # авторизовались и перенаправились на главную

    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)  # пост запрос через форму, аудит
        if form.is_valid():
            form.save()             # сохранить нового пользователя в БД
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)
