from django.contrib import admin
from django.urls import path, include

from clinic.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('services/', include('services.urls', namespace='services'))

] 

if DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
        ]
