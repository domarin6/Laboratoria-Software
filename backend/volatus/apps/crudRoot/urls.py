from django.urls import path
from . import views
from apps.crudRoot.viewsLogin import Login, Logout

urlpatterns = [
    path('Login/', Login.as_view(), name = 'Login'),
    path('Logout/', Logout.as_view(), name = 'Logout'),
    path('', views.crudRootView, name='crud-Root-View'),
    path('administradores-list/', views.administradoresList, name='administradores-list'),
    path('administradores-detail/<str:pk>/', views.administradorDetail, name='administradores-detail'),
    path('administradores-create/', views.administradorCreate, name='administradores-create'),
    path('administradores-update/<str:pk>/', views.administradorUpdate, name='administradores-update'),
    path('administradores-delete/<str:pk>/', views.administradorDelete, name='administradores-delete'),

]
