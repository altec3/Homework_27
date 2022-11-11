from django.contrib import admin
from django.urls import path, include

from ads import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cat/', include("categories.urls")),
    path('ad/', include("ads.urls")),
]
