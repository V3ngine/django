
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


from . forms import RegisterUserForm, LoginUserForm
from . models import Category

# Create your views here.


class HomeView(ListView):
    model = Category
    template_name = 'homepage.html'
    context_object_name = 'libs'
    queryset = Category.objects.all()

        
class RegisterUser(CreateView):
    template_name = 'registr.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('Books:home')

    def authorize(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Books:home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('Books:home')


class Library(ListView):
    pass


def logout_user(request):
        logout(request)
        return redirect('Books:home')


