from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='tohffa-home'),
    path('s/', views.search, name='search'),
    path('about/', views.about, name='tohffa-about'),
    path('return-policy/', views.returnpolicy, name='tohffa-return-policy'),
    path('terms-and-conditions/', views.tnc, name='tohffa-terms-and-conditions'),
    path('all/', views.all, name='all-products'),
    re_path(r'products/(?P<slug>[\w\-]+)/$', views.single, name='single-product'),
    re_path(r'(?P<slug>[\w\-]+)/$', views.producttype, name='product-type'),


]
