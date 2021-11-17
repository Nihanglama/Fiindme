from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .filters import OrderFilter
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from .decorators import permissions
from .forms import Customer_form,Product_form,Place_order
from django.contrib.messages import success


@login_required(login_url='login')
@permissions(allowed_to=['admin'])
def Dashboard(request):
          template='Manager/dashboard.html'
          order=Order.objects.all()
          customer=Customer.objects.all()
          total_order=order.count()
          complete_order=order.filter(status='Delivered').count()
          pending=total_order - complete_order
          objects={'orders':order,'total_order':total_order,'complete_order':complete_order,'pending':pending,'al_customers':customer}

          return render(request,template,objects)


class Products(LoginRequiredMixin,ListView):
      #     permission_required=['admin']
          model=Product
          template_name='Manager/products.html'
          context_object_name='products'
                
          def get_context_data(self, **kwargs):
              context = super().get_context_data(**kwargs)
              search_input=self.request.GET.get('search_area')
              if search_input:
                    context["products"] = context["products"].filter(name__icontains=search_input)
              context['search_input']=search_input

              return context
          

@login_required(login_url='login')
@permissions(allowed_to=['admin'])
def Profile(request,pk_cus):
          customer=Customer.objects.get(id=pk_cus)
          orders=customer.order_set.all()
          total_order=orders.count()
          search_input=OrderFilter(request.GET,queryset=orders)
          orders=search_input.qs
          context={'customer':customer,'orders':orders,'total_order':total_order,'search_input':search_input}
          

          template='Manager/customer.html'

          return render(request,template,context)


class Create_order(LoginRequiredMixin,CreateView):
      # permission_required=['admin']
      model=Order
      template_name='Manager/create_order.html'
      fields=['name','phone','customer','address']
      success_url=reverse_lazy('dashboard')     

      def form_valid(self, form):
            form.instance.user=self.request.user
            return super(Create_order,self).form_valid(form)


class Update_order(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
      permission_required=['admin']
      model=Order
      template_name='Manager/update_order.html'
      context_object_name='order'
      fields=['name','status','address']
      success_url=reverse_lazy('dashboard')

class Delete_order(LoginRequiredMixin,DeleteView):
      #     permission_required=['admin','customer']
          model=Order
          template_name='Manager/delete_order.html'
          context_object_name='order'
          def get_success_url(self):
                if self.request.user.is_staff:
                      return reverse_lazy('dashboard')
                else:
                      return reverse_lazy('customer_dashboard')

              



@login_required(login_url='login') 
@permissions(allowed_to=['admin'])
def Order_info(request,pk_ord):
          order=Order.objects.get(id=pk_ord)
          template='Manager/ordered_info.html'
          
          return render(request,template,{'order':order})



class Cus_update(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
          permission_required=['admin']
          model=Customer
          context_object_name='customer'
          template_name='Manager/update_cus_info.html'
          fields=['email','phone']
          success_url=reverse_lazy('dashboard')


@login_required(login_url='login')
@permissions(allowed_to=['customer'])
def customer_dashboard(request):
      template='Manager/customer_dashboard.html'

      orders=request.user.customer.order_set.all()
      total_order=orders.count()
      complete_order=orders.filter(status='Delivered').count()
      pending=total_order-complete_order
      delivered= orders.filter(status='Delivered')
      

      context={'orders':orders,'total_order':total_order,'complete_order':complete_order,'pending':pending,'delivered':delivered}

      return render(request,template,context)

@permissions(allowed_to=['customer'])
def customer_profile(request):
      template='Manager/customer_profile.html'
      form=Customer_form(instance=request.user.customer)

      if request.method=="POST":
            form=Customer_form(request.POST,request.FILES,instance=request.user.customer)
            if form.is_valid():
                  form.save()
                  success(request,'Profile updated successfully')                

      context={'form':form}
      return render(request,template,context)

def Add_Product(request):
      template='Manager/add_product.html'
      form=Product_form()
      if request.method=='POST':
            form=Product_form(request.POST,request.FILES)
            if form.is_valid():
                  form.save()

                  return redirect('product')
      context={'form':form}
      return render(request,template,context)



def Delete_product(request,pk_pro):
      product=Product.objects.get(pk=pk_pro)
      product.delete()

      return redirect('product')
      
class Place_order(LoginRequiredMixin,CreateView):
      model=Order
      template_name='Manager/place_order.html'
      fields=['name','phone','address']
      success_url=reverse_lazy('product')     

      def form_valid(self, form):
            form.instance.customer=self.request.user.customer
            return super(Place_order,self).form_valid(form)

      