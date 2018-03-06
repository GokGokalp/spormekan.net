"""spormekan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from api import views


schema_view = get_swagger_view(title='Spormekan.net API')
router = routers.DefaultRouter()
router.register(r'firms', views.FirmViewSet)
router.register(r'firm-preferences', views.FirmPreferenceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^backend-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', schema_view),
    url(r'^', include(router.urls))
]
