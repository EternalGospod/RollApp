"""
URL configuration for eternal_roll project.

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
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
# from coolsite import settings
from news.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
    )


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('news/', NewsAPIList.as_view()),
    path('news/<int:pk>/', NewsAPIUpdate.as_view()),
    path('newsdelete/<int:pk>/', NewsAPIDestroy.as_view()),
    path('charlist/',  CharListAPI.as_view()),
    path('charlist/<int:pk>/',  CharListAPIUpdate.as_view()),
    path('statblock/',  StatBlockAPI.as_view()),
    path('statblock/<int:pk>/',  StatBlockAPIUpdate.as_view()),
    path('auth/', include('djoser.urls')),

]