# from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import User,Manufacturer
from .forms import UserCreate,EditUser,CreateItems
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
class Home(TemplateView):
    template_name = 'home.html'

class Login(LoginView):
    '''login class '''
    template_name = 'login.html'
    success_url ='/'
    success_message = "Thing was deleted successfully."

class CreateUser(LoginRequiredMixin,CreateView):
    # model = User
    form_class = UserCreate
    template_name = 'register.html'
    # success_url = 'user_list'

    def post(self, request, *args, **kwargs):
        '''create employee post request'''
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # print("vnjfbvfvbb")
        ''' create employee form valid or not.'''
        form.save()
        messages.success(request=self.request, message="successfully create")
        super().form_valid(form)
        return super().form_valid(form)
        # return redirect('user_list')

    def get_success_url(self):
        ''''creae employee form and redirect url'''
        return reverse_lazy('user_list')

class UserList(LoginRequiredMixin,ListView):
    template_name = 'user_list.html'
    model = User
    queryset = User.objects.filter(is_deleted = False)
    context_object_name = 'user'

class UserEdit(UpdateView):
    template_name ='user_edit.html'
    form_class = EditUser
    model = User
    success_url = reverse_lazy('user_list')

    def post(self, request, *args, **kwargs):
        messages.success(request=self.request, message="successfully Updated")
        return super().post(request, *args, **kwargs)

class UserDelete(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')

    def post(self, request, *args, **kwargs):
        ''''employee delete post method'''
        user_details = User.objects.get(id=kwargs['pk'])
        print(user_details)
        user_details.is_deleted = True
        user_details.save()
        messages.success(request=self.request, message="successfully Deleted.")
        return HttpResponseRedirect(self.success_url)

class AddItems(LoginRequiredMixin,CreateView):
    # model = Manufacturer
    template_name = 'add_items.html'
    form_class = CreateItems
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     '''create employee post request'''
    #     return super().post(request, *args, **kwargs)

class ItemsList(LoginRequiredMixin,ListView):
    model = Manufacturer
    template_name = 'items_list.html'
    context_object_name = 'items'
    