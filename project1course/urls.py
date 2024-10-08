"""
URL configuration for project1course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home,name='home'),
    path('',getdata,name='getdata'),
    path('course/',course_view,name="course"),
    path('login/',login_view,name="login"),
    path('register/',register,name="register"),
    path('logout/',logout_view,name="logout"),
    path('profile/',profile,name='profile'),
    path('addcart/<int:id>',add_to_cart,name='addcart'),
    path('removecart/<int:id>',remove_cart,name='removecart'),
    path('delcart/<int:id>',del_cartitem,name='delcart'),
    path('coursedata/',coursedata,name='coursedata'),
    path('viewcart/',View_cart,name='viewcart'),
    path('search/',search_product,name='search')
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_DIR)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)