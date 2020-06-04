"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='main'),
    path('create/', views.GroupCreateView.as_view(), name='create'),
    path('join/<int:pk>', views.GroupJoinView.as_view(), name='join'),
    path('update/<int:pk>', views.GroupUpdateView.as_view(), name='update'),
    path('details/<slug:slug>/', views.GroupDetailView.as_view(), name='detail'),
    path('delete/<slug:slug>/', views.GroupDeleteView.as_view(), name='delete'),
]
