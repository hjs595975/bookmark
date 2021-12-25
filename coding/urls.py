from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bookmark/', include('bookmark.urls')),
    path('admin/', admin.site.urls),
]
