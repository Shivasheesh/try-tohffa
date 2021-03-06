"""tohffa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include, re_path
from users import views as user_views
from carts import views as cart_views
from orders import views as order_views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name='register'),
    path('profile/',user_views.profile, name='profile'),
    path('cart/', cart_views.view, name='cart'),
    path('checkout/', order_views.checkout, name='checkout'),
    path('orders/', order_views.orders, name='orders'),
    re_path(r'cart/(?P<id>\d+)/$', cart_views.remove_from_cart, name='remove_from_cart'),
    re_path(r'cart/(?P<slug>[\w\-]+)/$', cart_views.add_to_cart, name='add_to_cart'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    path('', include('products.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    