from django import views
from django.urls import path,include
from .views import  *
from .router import router

urlpatterns = [
    path("register/",View_Register),
    path("",include(router.urls)),
    path("expert/",Api_Expert), 
    path("post_reyting/",View_Post_Reyting),    
    path("search/",Api_Search_Expert),
    path("task_history/",Api_Task_History),
    path("user_task/",Api_Get_User_Task),
    path("expert/<int:pk>/",Api_Get_Expert),
    path('info_num', Api_Counter),
    path("post_bajarilgan/",Api_Done_User_Task),
    path("get_bajarilgan/",Api_History_User_Task),
    path("get_history/",Api_All_History_User_Task),
    path('get_dietolog/',ListDietolog.as_view())
]
