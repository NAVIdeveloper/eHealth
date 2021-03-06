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
    path("kirish/",loginpage),
    path("email/",is_email_user),
    path('get_dietolog/',Api_Dietolog),
    path("get_treyner/",Api_Sportsmen),
    path("user/",Api_Get_User),
    path('get_user/<int:id>/', get_user),
    
    path("admin_user/",Api_Admin_Login),
    path("admin_password/",Api_Admin_Change_Password),

    path("update_user/",Api_Update_User),
    path("contact/",ContactUs_Post),
    path("contact_get/",ContactUs_Get),
]