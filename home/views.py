from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import SearchForm
from .models import Person


# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Person
    context_object_name = 'persons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            name_search = Q(name__icontains=search)
            bio_search = Q(bio__icontains=search)
            queryset = queryset.filter(name_search | bio_search)
        return queryset


class DetailsPageView(DetailView):
    template_name = 'detail.html'
    model = Person

    def get(self, request, *args, **kwargs):
        print(request.path)
        return super().get(request, *args, **kwargs)


class CreatePersonView(CreateView):
    template_name = 'create.html'
    model = Person
    fields = '__all__'

    # success_url = reverse_lazy('home:home')
    def get_success_url(self):
        return reverse_lazy('home:detail', kwargs={'pk': self.object.pk})


class DeletePersonView(DeleteView):
    model = Person
    success_url = reverse_lazy('home:home')
    # template_name = 'detail.html'
    template_name = 'delete.html'


class UpdatePersonView(UpdateView):
    template_name = 'update.html'
    model = Person
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('home:detail', kwargs={'pk': self.object.pk})


class LoginPageView(AuthLoginView):
    template_name = 'login.html'
    next_page = 'home:home'

    def get(self, request, *args, **kwargs):
        print(request.path)  # Print request path to terminal
        return super().get(request, *args, **kwargs)


class LogoutPageView(LogoutView):
    next_page = 'home:home'
