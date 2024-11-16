from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,UpdateView
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.contrib.auth.models  import User
from .forms import register_user,update_form
from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


class home(TemplateView):
    template_name='home.html'



class create_account(CreateView):
    model=User
    form_class=register_user
    template_name='register.html'
    success_url=reverse_lazy('login')
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = " User Create"
        return context
    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request,"Account Created Successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return self.render_to_response(self.get_context_data(form=form))
   

class Log_in(LoginView):
    template_name='login.html'
    success_url=reverse_lazy('profile')
    
    def get_success_url(self):
        return self.success_url
    
    def form_valid(self, form):
        messages.success(self.request,"Logged in Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return super().form_invalid(form)

@method_decorator(login_required,name='dispatch')
class profile(TemplateView):
    template_name='profile.html'
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["user"] =self.request.user
        return context
    


def logout(request):
    auth.logout(request)
    return redirect('login')

@method_decorator(login_required,name='dispatch')
class edit_profile(UpdateView):
    model=User
    form_class=update_form
    template_name='register.html'
    pk_url_kwarg='pk'
    success_url=reverse_lazy('profile')
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Update Profile"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Profile Updated Successfully")
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class change_pass(PasswordChangeView):
    template_name='register.html'
    success_url = reverse_lazy('profile')
    def get_context_data(self, **kwargs) -> dict[str,]:
        context = super().get_context_data(**kwargs)
        context["type"] = "Password Change"
        return context
    def form_valid(self,form):
        messages.success(self.request,"Password Updated Done")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,"Something Went Wrong")
        return super().form_invalid(form)
        
        
    

    