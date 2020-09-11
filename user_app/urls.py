from django.urls import path
from user_app import views
from django.contrib.auth import views as auth_veiw

urlpatterns = [
    path('register', views.register,name='register'),
    path('login', auth_veiw.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout', auth_veiw.LogoutView.as_view(template_name='logout.html'),name='logout'),
]
