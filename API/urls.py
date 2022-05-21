from django.urls import path,include
from .views import  *
from .router import router

urlpatterns = [
    path("register/",View_Register),
    
    path("",include(router.urls)),
]