from django.urls import path
from apps.crudRoot.viewsLogin import Login, Logout, UserToken
from apps.crudRoot.views import UserCliente
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('Login/', Login.as_view(), name = 'Login'),
    path('Logout/', Logout.as_view(), name = 'Logout'),
    path('', views.crudRootView, name='crud-Root-View'),
    path('refresh-token/', UserToken.as_view(), name = 'refresh_token'),
    path('administradores-list/', views.administradoresList, name='administradores-list'),
    path('administradores-detail/<str:pk>/', views.administradorDetail, name='administradores-detail'),
    path('administradores-create/', views.administradorCreate, name='administradores-create'),
    path('administradores-update/<str:pk>/', views.administradorUpdate, name='administradores-update'),
    path('administradores-delete/<str:pk>/', views.administradorDelete, name='administradores-delete'),
    path('cliente', csrf_exempt(UserCliente.as_view()) , name='clientes'),

]
