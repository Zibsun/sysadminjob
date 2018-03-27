from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.listing, name='index'),
    path('<int:id>/', views.detail, name='detail'),
]