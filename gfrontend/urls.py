from django.urls import path
from gfrontend import views

urlpatterns = [
    path('gamepage/', views.gamepage, name='gamepage'),
    path('game1/', views.game1, name='game1'),
    path('game1_filtered/<cat_name>/', views.game1_filtered, name='game1_filtered'),
    path('sprod/<int:proid>/', views.sprod, name='sprod'),
    path('abtus/', views.abtus, name='abtus'),
    path('contact_page/', views.contact_page, name='contact_page'),
    path('contactdata/', views.contactdata, name='contactdata'),
    path('services_page/', views.services_page, name='services_page'),

    path('register_page/', views.register_page, name='register_page'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('UserLogin/', views.UserLogin, name='UserLogin'),
    path('User_logout/', views.User_logout, name='User_logout'),

    path('Cart_page/', views.Cart_page, name='Cart_page'),
    path('cartdata/', views.cartdata, name='cartdata'),
    path('cart_delete/<int:pro_id>/', views.cart_delete, name='cart_delete'),

    path('checkout_page/', views.checkout_page, name='checkout_page'),
]