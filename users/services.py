from django.contrib import auth
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from users.forms import UserRegistrationForm, UserLoginForm


class LoginService(View):
    @staticmethod
    def get(request):
        form = UserLoginForm()
        context = {'login_form': form}
        return render(request, 'users/login.html', context=context)

    @staticmethod
    def post(request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            LoginService._handle_valid_form(request, form)
            return redirect(reverse('core:index_page'))

        context = {'login_form': form}
        return render(request, 'users/login.html', context=context)

    @staticmethod
    def _handle_valid_form(request, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect(reverse('core:index_page'))


class RegistrationService(View):

    @staticmethod
    def get(request):
        form = UserRegistrationForm()
        context = {'register_form': form}
        return render(request, 'users/login.html', context=context)

    @staticmethod
    def post(request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            RegistrationService._handle_valid_form(request, form)
            return redirect(reverse('core:index_page'))

        context = {'register_form': form}
        return render(request, 'users/login.html', context=context)

    @staticmethod
    def _handle_valid_form(request, form):
        form.save()
        user = form.instance
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')


class LogoutService(View):
    @staticmethod
    def get(request):
        auth.logout(request)
        return redirect(reverse('core:index_page'))
