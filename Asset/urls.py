from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Created a new urls file on my Api app and included the urls file here
    path('', include('Api.urls')),
]
