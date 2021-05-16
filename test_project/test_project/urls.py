from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('myapps/', include('myapps.urls')),
    path('admin/', admin.site.urls),
]

