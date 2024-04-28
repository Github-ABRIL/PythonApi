from django.contrib import admin
from django.urls import path
from IPNpy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conversation/', views.index, name='conversation'),
]
