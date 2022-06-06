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
]

