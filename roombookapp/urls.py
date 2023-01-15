from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.base),
    path('bookfind',views.bookfind),
    path('bookform',views.bookform),
    path('login',views.login),
    path('logout',views.logout),
]