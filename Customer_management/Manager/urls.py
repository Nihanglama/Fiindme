from django.urls import path
from .import views
from .views import *

urlpatterns = [
          path('',views.Dashboard,name='dashboard'),
          path('product/',Products.as_view(),name='product'),
          path('customer/<str:pk_cus>/',views.Profile,name='customer'),
          path('create_order',Create_order.as_view(),name='create_order'),
          path('update_order/<int:pk>/',Update_order.as_view(),name='update_order'),
          path('delete_order/<int:pk>/',Delete_order.as_view(),name='delete_order'),
          path('order_info/<int:pk_ord>/',views.Order_info,name='order_info'),
          path('customers_info_update/<str:pk>/',Cus_update.as_view(),name='update_cus_info'),
          path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),      
          path('customer_profile/',views.customer_profile,name='customer_profile'),  
          path('add_product/',views.Add_Product,name='add_p'),
          path('delete_product/<int:pk_pro>/',Delete_product,name='delete_product'),
          path('place_order/',Place_order.as_view(),name='place_order'),
    
]