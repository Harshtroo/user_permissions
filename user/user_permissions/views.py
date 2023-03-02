# from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .models import User
from .forms import UserCreate


class Home(TemplateView):
    template_name = 'home.html'

class CreateUser(CreateView):
    model = User
    form_class = UserCreate
    template_name = 'register.html'
    
    def post(self, request, *args, **kwargs):
        '''create employee post request'''
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
            ''' create employee form valid or not.'''
            form.save()
            messages.success(request=self.request, message="successfully create")
            super().form_valid(form)
            return redirect('user_list')

class UserList(ListView):
    template_name = 'user_list.html'
    model = User
    # queryset = User.objects.filter(is_deleted = False)
    context_object_name = 'user'