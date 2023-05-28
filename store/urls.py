from django.contrib import admin
from django.urls import path
from .views.home import Index, store, home, condiciones_uso, privacidad
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.perfil import view_profile, edit_profile
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home', home, name='home'),
    path('condiciones', condiciones_uso, name='condiciones'),
    path('privacidad', privacidad, name='privacidad'),

    path('store', store, name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),

    path('perfil/', auth_middleware(view_profile), name='perfil'),
    path('perfil/edit/', auth_middleware(edit_profile), name='edit_perfil'),

    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
]
