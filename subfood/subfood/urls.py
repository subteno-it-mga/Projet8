"""subfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url

from comparate import views

urlpatterns = [
    path('',views.BasicViews.index, name="index"),
    path('admin/', admin.site.urls),
    path('comparate/', include('comparate.urls')),
    path('signup/',views.UserAccount.signup,name="signup"),
    path('logout_user/',views.UserAccount.logout_user,name="logout_user"),
    path('login_user/',views.UserAccount.login_user,name="login_user"),
    path('user_account/', views.UserAccount.as_view(), name="user_account"),
    path('search/',views.search,name="search"),
    path('favorite/',views.BasicViews.favorite,name="favorite"),
    path('compare/',views.compare,name="compare"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns =[
        url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
