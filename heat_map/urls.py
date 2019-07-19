"""heat_map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

from heat_map.rest import IpvFourViewSet, IpvSixViewSet

apiRouter = routers.DefaultRouter(trailing_slash=False)
apiRouter.register(r'ipvfour', IpvFourViewSet, base_name='ipvfour')
apiRouter.register(r'ipvsix', IpvSixViewSet, base_name='ipvsix')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(apiRouter.urls)),
]

