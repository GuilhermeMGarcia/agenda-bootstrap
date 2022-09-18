from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.AccountsView.as_view(), name='accounts'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.register, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
