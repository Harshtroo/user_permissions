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
from django.contrib.auth.models import Group
from .mixin import MyCustomPermissions

class Home(TemplateView):
    template_name = 'home.html'

class Login(LoginView):
    '''login class '''
    template_name = 'login.html'
    # success_url ='user_list'
    success_message = "Thing was deleted successfully."
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

class Logout(LogoutView):
    '''logout class'''
    pass

class CreateUser(LoginRequiredMixin,CreateView):
    # model = User
    form_class = UserCreate
    template_name = 'register.html'
    # success_url = reverse_lazy('user_list')

    def post(self, request, *args, **kwargs):
        '''create employee post request'''
        user_form = self.form_class(request.POST or None)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            group = Group.objects.filter(name = user.role)
            user.save()
            if group:
                group = group.first()
                user.groups.add(group.id)
        return redirect(reverse_lazy('user_list'))

class UserList(MyCustomPermissions, ListView):
    login_url = 'login'
    template_name = 'user_list.html'
    model = User
    queryset = User.objects.filter(is_deleted = False)
    context_object_name = 'user'
    permission_required = ('user_permissions.view_user', 'user_permissions.change_user')

    def post(self,request,*args,**kwargs):
        messages.error(request=self.request, message="You are not authoricesd.")
        return super().post(request, *args, **kwargs)

class UserEdit(MyCustomPermissions, UpdateView):
    template_name ='user_edit.html'
    form_class = EditUser
    # model = User
    success_url = reverse_lazy('user_list')
    permission_required = ('user_permissions.view_user',)

    def get_queryset(self):
        return User.objects.all()

    def form_valid(self, form):
        group = Group.objects.filter(name = form.cleaned_data.get('role'))
        user = User.objects.get(email=form.cleaned_data.get('email'))
        if group:
            group = group.first()
            user.groups.clear()
            user.groups.add(group.id)
        return super(UserEdit, self).form_valid(form)

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
    login_url = 'login'
    # model = Manufacturer
    template_name = 'add_items.html'
    form_class = CreateItems
    success_url = '/'

    # def post(self, request, *args, **kwargs):
    #     '''create employee post request'''
    #     return super().post(request, *args, **kwargs)

class ItemsList(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Manufacturer
    template_name = 'items_list.html'
    context_object_name = 'items'
    