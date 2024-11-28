from . import views
from django.urls import path
from django.contrib.auth import views as authentication_views

urlpatterns = [
    #/index
    path('',views.index, name='index'),
    #/index/articulo
    path('articulo/<int:bicicleta_id>/',views.articulos, name='articulo'),
    #/index/registro
    path('registro/',views.register, name='registro'),
    #/index/login
    path('login/', views.login_view, name='login'),
    #/index/logout
    path('logout/', views.logout_view, name='logout'),
    #/index/perfil
    path('perfil/', views.user_profile, name='perfil'),
    #/index/checkout
    path('checkout/',views.checkout, name='checkout'),
]