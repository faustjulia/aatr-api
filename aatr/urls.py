from django.contrib import admin
from django.urls import path

from aatr.views import get_sample, signup_endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/', get_sample),
    path('api/signup/', signup_endpoint)
]
