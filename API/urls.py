from django.urls import path,include
from .views import  *
from .router import router

urlpatterns = [
    path("register/",View_Register),
    path("",include(router.urls)),
    path("expert/",Api_Expert), 
    path("post-reyting/",View_Post_Reyting),    
    path("search/",Api_Search_Expert),
]
