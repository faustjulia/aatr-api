"""aatr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import typing

import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested.routers import SimpleRouter

from aatr.views import signin, signup, signout, CurrentUserViewSet

viewsets: typing.List[typing.Dict] = [
    {
        'prefix': r'api/current_user',
        'viewset': CurrentUserViewSet,
        'basename': 'current_user'
    }
]

router = SimpleRouter()

for viewset in viewsets:
    router.register(
        prefix=viewset['prefix'],
        viewset=viewset['viewset'],
        basename=viewset['basename']
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signin/', signin, name='signin'),
    path('api/signup/', signup, name='signup'),
    path('api/signout/', signout, name='signout')
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))

urlpatterns += router.urls
