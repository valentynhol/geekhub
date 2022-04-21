from django.shortcuts import render
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LogInForm, SignUpForm
from .models import Card, BankAccount, User


def __user_login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect('../')
        else:
            context = {'form': form, 'error': "Неправильна електронна адреса або пароль!"}
    else:
        form = LogInForm()
        context = {'form': form}
    return render(request, 'login.html', context)


def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'cards.html', {'username': user})
    else:
        return __user_login(request)


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(email=request.POST['email'],
                                                password=request.POST['password1'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                patronymic=request.POST['patronymic'],
                                                phone_number=request.POST['phone_number'])
                if user:
                    login(request, user)
                    return HttpResponseRedirect('../')
                else:
                    context = {'form': form, 'error': "Неправильна електронна адреса або пароль!"}
            except IntegrityError as signup_error:
                context = {'form': form, 'error': 'Ця електронна адреса вже використовується'
                                                  if 'email' in str(signup_error)
                                                  else 'Цей номер телефону вже використовується'}

        else:
            context = {'form': form, 'error': "Паролі не збігаються!"}
    else:
        form = SignUpForm()
        context = {'form': form}
    return render(request, 'signup.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')
