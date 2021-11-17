from django.urls import path,include
from .views import Login
from .import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
          path('register/',views.Register,name='register'),
          path('login/',Login.as_view(),name='login'),
          path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
          path('reset_password/',auth_views.PasswordResetView.as_view(template_name='user_handler/reset_form.html'),name='reset_password'),
          path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='user_handler/message_sent.html'),name='password_reset_done'),
          path('reset_password/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user_handler/newpassform.html'),name='password_reset_confirm'),
          path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user_handler/resetdone.html'),name='password_reset_complete'),
]