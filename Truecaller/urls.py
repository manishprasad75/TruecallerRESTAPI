"""Truecaller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user import views
from mysite import views as spam
from search import views as search
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.registration),
    path('api/spam/', spam.SpamUser.as_view()),
    path('api/user/', spam.UserList.as_view()),
    path('api/search/', search.Search.as_view()),

]
