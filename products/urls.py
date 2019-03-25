from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tohffa-home'),
    path('s/', views.search, name='search'),
    path('about/', views.about, name='tohffa-about'),
    path('all/', views.all, name='all-products'),
    path('products/<slug:title>/' , views.single , name='single-product'),
]
  