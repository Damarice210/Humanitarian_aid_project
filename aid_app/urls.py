# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('distributions/', views.distribution_list, name='distribution_list'),
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relief.urls')),  # Include the URLs from the `relief` app
]
