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

from django.conf import settings
from django.conf.urls.static import static

# router = routers.DefaultRouter()
# router.register(r'news', NewsViewSet, basename='news')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('news.urls'),)
    # re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('admin/', admin.site.urls),
    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/news/', NewsAPIList.as_view()),
    # path('api/v1/news/<int:pk>/', NewsAPIUpdate.as_view()),
    # path('api/v1/newsdelete/<int:pk>/', NewsAPIDestroy.as_view()),
    # path('api/v1/auth/', include('djoser.urls')),
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        # path('api/v1/', include(router.urls)), 
    # path('api/v1/news', NewsViewSet.as_view({'get': 'list'})), # описываев {} какой метод при каком з апросе будет вызыв
    # path('api/v1/news/<int:pk>', NewsViewSet.as_view({'put': 'update'})),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)