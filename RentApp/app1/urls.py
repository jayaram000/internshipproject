"""
URL configuration for RentApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from app1 import views
app_name="app1"


urlpatterns = [path('',views.home,name="home"),
               path('items/',views.items,name="items"),
               path('upload/',views.upload,name="upload"),
               path('category/<n>',views.category,name="category"),
               path('register/',views.register,name="register"),
               path('login/',views.user_login,name="login"),
               path('logout/',views.user_logout,name="logout"),
               path('itemdetail/<int:pk>/', views.item_detail, name='itemdetail'),
               path('useruploads/',views.user_uploads,name="useruploads"),
               path('update/<int:pk>',views.update,name="update"),
               path('deletepost/<int:pk>',views.post_delete,name="delete"),
               path('favourite/<int:pk>/', views.favourite, name='fav'),
               path('fav/',views.favor_view,name="fav_view"),
               path('request_form/<int:pk>',views.request_form,name="requestform"),
               path('view_booking_requests/',views.view_booking_requests,name="bookreq"),
               path('reply-booking-request/<int:pk>/', views.reply_booking_request, name='reply_booking_request'),
               path('view_your_requests',views.view_request,name="viewreq")




]


