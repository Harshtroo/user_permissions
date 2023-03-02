# from django.shortcuts import render
# from django.views.generic import TemplateView,CreateView
# from .models import User
# from .forms import RegisterForm


# class Home(TemplateView):
#     template_name = 'home.html'

# class Register(CreateView):
#     model = User
#     form_class = RegisterForm
#     template_name = 'register.html'
    
#     def post(self, request, *args, **kwargs):
#         '''create employee post request'''
#         return super().post(request, *args, **kwargs)