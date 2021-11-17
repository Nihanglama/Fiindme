from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.messages import success
from Manager.models import Customer
from Manager.forms import Signup

                    
def Register(request):

      if request.user.is_authenticated:
            return redirect('dashboard')

      form=Signup()
      template='user_handler/register.html'
      if request.method=='POST':
            form=Signup(request.POST)
            if form.is_valid():
                  user=form.save()
                  username=form.cleaned_data.get('username')
                  success(request,'Account Created Successfully!')
                  return redirect('login')

      context_object= {'form':form}           
      return render(request,template,context_object)


class Login(LoginView):
          template_name='user_handler/login.html'
          fields='__all__'
          def get_success_url(self):
                if self.request.user.groups.all()[0].name =='admin':
                      return reverse_lazy('dashboard')
                else:
                      return reverse_lazy('customer_dashboard')
 
          def get(self,*args, **kwargs):
                if self.request.user.is_authenticated and self.request.user.groups.all()[0].name =='admin':
                        success(self.request,"Login Successful!")
                        return redirect('dashboard')
                elif self.request.user.is_authenticated and self.request.user.groups.all()[0].name =='customer':
                      return redirect('customer_dashboard')

                return super(Login, self).get(*args, **kwargs)      

     
          



          

          