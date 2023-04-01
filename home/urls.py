from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('add_product', views.add_product, name='add_product'),
    path('admin_users', views.admin_users, name='admin_users'),
    path('admin', views.admin, name='admin'),
    path('contactus', views.contactus, name='contactus'),
    path('login', views.login, name='login'),
    path('manage_product', views.manage_product, name='manage_product'),
    path('notification', views.notification, name='notification'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('add_productcars', views.add_productcars, name = 'add_productcars'),
    path('add_productmobiles', views.add_productmobiles, name = 'add_productmobiles'),
    path('add_productlaptops', views.add_productlaptops, name = 'add_productlaptops'),
    path('bikes_page', views.bikes_page, name = 'bikes_page'),
    path('cars_page', views.cars_page, name = 'cars_page'),
    path('laptops_page', views.laptops_page, name = 'laptops_page'),
    path('mobiles_page', views.mobiles_page, name = 'mobiles_page'),
    path('test', views.test, name = 'test'),
    path('edit/<int:id>&<str:catagory>', views.edit, name = 'edit'),
    path('update/<int:id>&<str:catagory>', views.update, name='update'),
    path('admin_update/<int:id>&<str:catagory>', views.admin_update, name='admin_update'),
    path('delete/<int:id>&<str:catagory>' , views.delete , name='delete'),
    path('admin_delete/<int:id>&<str:catagory>' , views.admin_delete , name='admin_delete'),
    path('adminlogin', views.adminlogin, name = 'adminlogin'),
    path('delete_user/<int:id>&<str:username>', views.delete_user, name = 'delete_user'),
    path('view_product/<int:id>&<str:catagory>', views.view_product, name = 'view_product'),
    path('admin_products', views.admin_products, name='admin_products'),
    path('admin_manage_product/<str:catagory>', views.admin_manage_product, name = 'admin_manage_product'),
    path('buy_now/<int:ProductId>&<str:ProductName>&<str:SellerName>&<str:UserName>', views.buy_now, name = 'buy_now'),
    path('submit', views.submit, name = 'submit'),
    path('search', views.search, name = 'search'),
    path('userinfo', views.userinfo, name = 'userinfo'),
]

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

# urlpatterns = [
# 	path('add_product', add_product, name = 'add_product'),
# 	# path('success', success, name = 'success'),
# ]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
							document_root=settings.MEDIA_ROOT)
