from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    url(r'^data/',include('data_entry.urls')),
    url(r'^admin/', admin.site.urls),
]
