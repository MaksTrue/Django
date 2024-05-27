from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse

from .forms import RegistarationForm
from django.views.generic import CreateView, DeleteView
from .models import ParserUser
from rest_framework.authtoken.models import Token


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = ParserUser
    template_name = 'userapp/registration.html'
    form_class = RegistarationForm
    success_url = reverse_lazy('user:login')


class UserDeleteView(DeleteView):
    template_name = 'userapp/profile.html'
    model = ParserUser


def update_token(request):
    user = request.user
    if user.auth_token:
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        Token.objects.create(user=user)

    return HttpResponseRedirect(reverse('user:profile', kwargs={'pk': user.pk}))