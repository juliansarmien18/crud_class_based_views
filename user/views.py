from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import User


class UserList(ListView):
    model = User


class UserDetail(DetailView):
    model = User


class UserCreation(CreateView):
    model = User
    success_url = reverse_lazy('user:list')
    fields = ['name', 'email', 'phone']


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('user:list')
    fields = ['name', 'email', 'phone']


class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user:list')
