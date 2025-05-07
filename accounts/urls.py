from django.urls import path
from .views import (
    signup,signin,signout,profile
)

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='login'),
    path('signout/',signout,name='logout'),
    path('profile/',profile,name='profile')
]